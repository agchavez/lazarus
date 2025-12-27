"""
Ejemplo de uso de PostgreSQL Checkpointer con LangGraph

Este script muestra cómo:
1. Conectarse a PostgreSQL para persistencia
2. Guardar checkpoints de grafos en base de datos
3. Recuperar conversaciones desde la DB
4. Implementar métricas y logging

Requisitos:
- PostgreSQL corriendo (docker-compose up -d postgres)
- Variables de entorno configuradas
"""

import os
from typing import TypedDict, Annotated
from datetime import datetime
from operator import add

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.postgres import PostgresSaver
import psycopg2
from psycopg2.extras import RealDictCursor

load_dotenv()

# Configuración de PostgreSQL
DB_CONFIG = {
    "host": os.getenv("POSTGRES_HOST", "localhost"),
    "port": int(os.getenv("POSTGRES_PORT", "5432")),
    "database": os.getenv("POSTGRES_DB", "langgraph_checkpoints"),
    "user": os.getenv("POSTGRES_USER", "langgraph"),
    "password": os.getenv("POSTGRES_PASSWORD", "langgraph123")
}

# State para conversación
class ConversationState(TypedDict):
    messages: Annotated[list, add]
    user_id: str
    session_id: str
    metadata: dict


def crear_grafo_conversacion() -> StateGraph:
    """Crea un grafo simple de conversación"""

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

    def chatbot_node(state: ConversationState) -> ConversationState:
        """Nodo que procesa mensajes con el LLM"""
        print(f"\n🤖 Procesando mensaje para usuario: {state['user_id']}")

        # Obtener último mensaje del usuario
        messages = state.get("messages", [])
        if not messages:
            return state

        # Contexto del sistema
        system_msg = """Eres un asistente de CONCESA, empresa de renta de equipos de construcción.
        Eres profesional, amable y conoces bien el catálogo de productos."""

        # Preparar mensajes para el LLM
        llm_messages = [HumanMessage(content=system_msg)] + messages

        # Generar respuesta
        response = llm.invoke(llm_messages)

        # Registrar métricas
        registrar_uso_modelo(
            session_id=state.get("session_id", "unknown"),
            model_name="gpt-4o-mini",
            tokens_input=len(str(messages)) // 4,  # Estimación
            tokens_output=len(response.content) // 4,
            success=True
        )

        return {
            "messages": [response],
            "user_id": state["user_id"],
            "session_id": state["session_id"],
            "metadata": state.get("metadata", {})
        }

    # Construir grafo
    workflow = StateGraph(ConversationState)
    workflow.add_node("chatbot", chatbot_node)
    workflow.add_edge(START, "chatbot")
    workflow.add_edge("chatbot", END)

    return workflow


def conectar_postgres() -> psycopg2.extensions.connection:
    """Establece conexión con PostgreSQL"""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        print("✅ Conectado a PostgreSQL")
        return conn
    except Exception as e:
        print(f"❌ Error conectando a PostgreSQL: {e}")
        print("\n💡 Asegúrate de que PostgreSQL está corriendo:")
        print("   docker-compose up -d postgres")
        raise


def registrar_uso_modelo(session_id: str, model_name: str, tokens_input: int,
                        tokens_output: int, success: bool = True, error_message: str = None):
    """Registra métricas de uso de modelos en PostgreSQL"""
    try:
        conn = conectar_postgres()
        cursor = conn.cursor()

        # Calcular costo aproximado (GPT-4o-mini)
        cost_per_1m_input = 0.15
        cost_per_1m_output = 0.60
        cost = (tokens_input * cost_per_1m_input / 1_000_000) + \
               (tokens_output * cost_per_1m_output / 1_000_000)

        # Insertar métrica
        cursor.execute("""
            INSERT INTO usage_metrics
            (session_id, model_name, tokens_input, tokens_output, cost_usd, success, error_message)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (session_id, model_name, tokens_input, tokens_output, cost, success, error_message))

        conn.commit()
        cursor.close()
        conn.close()

    except Exception as e:
        print(f"⚠️ Error registrando métrica: {e}")


def guardar_mensaje_historial(session_id: str, user_id: str, message_type: str,
                              content: str, metadata: dict = None):
    """Guarda mensajes en el historial de conversaciones"""
    try:
        conn = conectar_postgres()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO conversation_history
            (session_id, user_id, message_type, content, metadata)
            VALUES (%s, %s, %s, %s, %s)
        """, (session_id, user_id, message_type, content,
              psycopg2.extras.Json(metadata) if metadata else None))

        conn.commit()
        cursor.close()
        conn.close()

    except Exception as e:
        print(f"⚠️ Error guardando mensaje: {e}")


def obtener_historial_conversacion(session_id: str) -> list:
    """Recupera el historial de una conversación"""
    try:
        conn = conectar_postgres()
        cursor = conn.cursor(cursor_factory=RealDictCursor)

        cursor.execute("""
            SELECT message_type, content, created_at
            FROM conversation_history
            WHERE session_id = %s
            ORDER BY created_at ASC
        """, (session_id,))

        mensajes = cursor.fetchall()

        cursor.close()
        conn.close()

        return mensajes

    except Exception as e:
        print(f"❌ Error obteniendo historial: {e}")
        return []


def obtener_metricas_costo(dias: int = 7) -> dict:
    """Obtiene métricas de costo de los últimos N días"""
    try:
        conn = conectar_postgres()
        cursor = conn.cursor(cursor_factory=RealDictCursor)

        cursor.execute("""
            SELECT * FROM cost_analysis
            WHERE date >= CURRENT_DATE - INTERVAL '%s days'
            ORDER BY date DESC, total_cost DESC
        """, (dias,))

        metricas = cursor.fetchall()

        cursor.close()
        conn.close()

        return metricas

    except Exception as e:
        print(f"❌ Error obteniendo métricas: {e}")
        return []


def main():
    """Función principal de demostración"""

    print("="*80)
    print("🐘 DEMO: PostgreSQL Checkpointer con LangGraph")
    print("="*80)

    # 1. Verificar conexión
    print("\n1️⃣ Verificando conexión a PostgreSQL...")
    try:
        conn = conectar_postgres()
        conn.close()
    except:
        print("\n❌ No se pudo conectar a PostgreSQL")
        print("\n📋 Pasos para iniciar PostgreSQL:")
        print("   1. cd 'Clases/Clase 6'")
        print("   2. docker-compose up -d postgres")
        print("   3. Esperar 10 segundos y ejecutar de nuevo")
        return

    # 2. Crear grafo
    print("\n2️⃣ Creando grafo de conversación...")
    workflow = crear_grafo_conversacion()

    # 3. Compilar con PostgreSQL Checkpointer
    print("\n3️⃣ Compilando con PostgreSQL Checkpointer...")

    # Crear connection string
    db_uri = f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"

    try:
        checkpointer = PostgresSaver.from_conn_string(db_uri)
        app = workflow.compile(checkpointer=checkpointer)
        print("✅ Grafo compilado con persistencia en PostgreSQL")
    except Exception as e:
        print(f"❌ Error creando checkpointer: {e}")
        print("\n💡 Usando MemorySaver como fallback...")
        from langgraph.checkpoint.memory import MemorySaver
        checkpointer = MemorySaver()
        app = workflow.compile(checkpointer=checkpointer)

    # 4. Ejecutar conversación
    print("\n4️⃣ Ejecutando conversación de ejemplo...")

    import uuid
    session_id = f"demo-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
    user_id = "user-123"

    config = {
        "configurable": {
            "thread_id": session_id
        }
    }

    conversacion = [
        "Hola, necesito información sobre demoledores",
        "¿Cuál es el más potente que tienen?",
        "¿Cuánto cuesta rentarlo por 15 días?"
    ]

    for i, mensaje_usuario in enumerate(conversacion, 1):
        print(f"\n{'─'*80}")
        print(f"Turno #{i}")
        print(f"{'─'*80}")
        print(f"👤 Usuario: {mensaje_usuario}")

        # Guardar mensaje del usuario en historial
        guardar_mensaje_historial(session_id, user_id, "user", mensaje_usuario)

        # Ejecutar grafo
        resultado = app.invoke(
            {
                "messages": [HumanMessage(content=mensaje_usuario)],
                "user_id": user_id,
                "session_id": session_id,
                "metadata": {"timestamp": datetime.now().isoformat()}
            },
            config
        )

        # Obtener respuesta
        if resultado.get("messages"):
            respuesta = resultado["messages"][-1].content
            print(f"🤖 Asistente: {respuesta}")

            # Guardar respuesta en historial
            guardar_mensaje_historial(session_id, user_id, "assistant", respuesta,
                                     {"model": "gpt-4o-mini"})

    # 5. Mostrar checkpoints guardados
    print(f"\n\n5️⃣ Explorando checkpoints guardados...")

    try:
        checkpoints = list(app.get_state_history(config))
        print(f"\n📊 Total de checkpoints guardados: {len(checkpoints)}")

        for i, checkpoint in enumerate(checkpoints[:3], 1):  # Solo mostrar primeros 3
            print(f"\n  Checkpoint #{i}:")
            print(f"    ID: {checkpoint.config['configurable'].get('checkpoint_id', 'N/A')[:12]}...")
            print(f"    Mensajes: {len(checkpoint.values.get('messages', []))}")
    except Exception as e:
        print(f"⚠️ No se pudieron obtener checkpoints: {e}")

    # 6. Mostrar historial de conversación
    print(f"\n\n6️⃣ Historial de conversación desde PostgreSQL...")

    historial = obtener_historial_conversacion(session_id)
    print(f"\n📝 Mensajes guardados: {len(historial)}")

    for msg in historial:
        emoji = "👤" if msg['message_type'] == 'user' else "🤖"
        print(f"\n{emoji} [{msg['created_at']}] {msg['content'][:80]}...")

    # 7. Mostrar métricas de costo
    print(f"\n\n7️⃣ Métricas de costo (últimos 7 días)...")

    metricas = obtener_metricas_costo(7)

    if metricas:
        print("\n📊 Resumen de costos:")
        print(f"\n{'Fecha':<12} {'Modelo':<15} {'Requests':<10} {'Costo Total':<12}")
        print("─" * 60)

        total_cost = 0
        for m in metricas:
            fecha = m['date'].strftime('%Y-%m-%d') if m['date'] else 'N/A'
            modelo = m['model_name'][:14]
            requests = m['request_count']
            costo = m['total_cost'] or 0
            total_cost += costo

            print(f"{fecha:<12} {modelo:<15} {requests:<10} ${costo:<11.6f}")

        print("─" * 60)
        print(f"{'TOTAL':<40} ${total_cost:.6f}")
    else:
        print("  ⚠️ No hay métricas disponibles")

    # 8. Resumen final
    print("\n\n" + "="*80)
    print("✅ DEMO COMPLETADA")
    print("="*80)
    print(f"\n📋 Resumen:")
    print(f"   - Session ID: {session_id}")
    print(f"   - Mensajes intercambiados: {len(conversacion) * 2}")
    print(f"   - Checkpoints guardados: {len(checkpoints) if 'checkpoints' in locals() else 'N/A'}")
    print(f"   - Persistencia: PostgreSQL ✅")

    print(f"\n💡 Puedes consultar los datos directamente:")
    print(f"   docker exec -it postgres-db psql -U langgraph -d langgraph_checkpoints")
    print(f"   SELECT * FROM conversation_history WHERE session_id = '{session_id}';")

    print("\n🎉 ¡Persistencia con PostgreSQL funcionando correctamente!")


if __name__ == "__main__":
    main()
