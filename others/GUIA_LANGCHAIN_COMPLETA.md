# 🔗 Guía Completa de LangChain - De Cero a Experto

> **Guía de estudio personal para dominar LangChain**
> Esta guía te ayudará a entender LangChain desde los fundamentos hasta conceptos avanzados.

---

## 📖 Índice

1. [¿Qué es LangChain?](#qué-es-langchain)
2. [LCEL: Lo Más Importante](#lcel-lo-más-importante)
3. [Conceptos Fundamentales](#conceptos-fundamentales)
4. [Componentes Principales](#componentes-principales)
5. [Guía de Estudio por Niveles](#guía-de-estudio-por-niveles)
6. [Patrones y Mejores Prácticas](#patrones-y-mejores-prácticas)
7. [Troubleshooting Común](#troubleshooting-común)
8. [LangGraph](#langgraph-workflows-complejos)
9. [Recursos de Aprendizaje](#recursos-de-aprendizaje)

---

## ¿Qué es LangChain?

### Definición Simple
**LangChain es un framework para construir aplicaciones con LLMs (Large Language Models).**

Piénsalo como un "LEGO" para IA:
- En vez de escribir código desde cero cada vez
- Usas bloques pre-construidos (componentes)
- Los conectas para crear aplicaciones complejas

### ¿Por qué usar LangChain?

#### ❌ Sin LangChain:
```python
# Código manual, repetitivo y difícil de mantener
import openai

def consultar_pdf(pregunta):
    # 1. Leer PDF (código personalizado)
    # 2. Dividir en chunks (código personalizado)
    # 3. Crear embeddings (código personalizado)
    # 4. Buscar similitud (código personalizado)
    # 5. Llamar OpenAI (código personalizado)
    # 6. Formatear respuesta (código personalizado)
    # = 200+ líneas de código
```

#### ✅ Con LangChain:
```python
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA

# 1. Cargar PDF
loader = PyPDFLoader("documento.pdf")
docs = loader.load()

# 2. Vectorizar
vectorstore = FAISS.from_documents(docs, OpenAIEmbeddings())

# 3. Crear sistema RAG completo
qa = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(),
    retriever=vectorstore.as_retriever()
)

# 4. Consultar
respuesta = qa.run("¿Cuál es el precio?")
# = 10 líneas de código
```

### Historia Rápida
- **2022**: Harrison Chase crea LangChain
- **2023**: Se vuelve el framework más popular para LLMs
- **2024**: Introducción de LCEL (LangChain Expression Language) - sintaxis moderna
- **2025**: Arquitectura modular con LangGraph, LangSmith, LangServe
- **Hoy**: Usado por empresas como Notion, Zapier, Klarna, Robinhood

### 🆕 ¿Qué es LCEL?

**LCEL (LangChain Expression Language)** es la forma moderna de construir chains en LangChain usando el operador pipe `|`.

**Ventajas de LCEL:**
- ✅ Código más limpio y legible
- ✅ Ejecución optimizada automáticamente
- ✅ Soporte nativo para streaming
- ✅ Soporte para ejecución paralela
- ✅ Soporte para async/await
- ✅ Integración automática con LangSmith (tracing)

**Ejemplo comparativo:**

```python
# ❌ Forma antigua (LLMChain - deprecado)
from langchain.chains import LLMChain

chain = LLMChain(llm=llm, prompt=prompt)
resultado = chain.run({"input": "hola"})

# ✅ Forma con LCEL (actual)
chain = prompt | llm | parser
resultado = chain.invoke({"input": "hola"})
```

---

## LCEL: Lo Más Importante

> **⚠️ IMPORTANTE**: Si aprendes LangChain en 2025, debes aprender LCEL. Es la forma estándar de trabajar con LangChain.

### ¿Qué cambió en LangChain?

En versiones anteriores de LangChain, usabas **clases** como `LLMChain`, `ConversationChain`, etc.

**Ahora (2025)**, usas **LCEL (LangChain Expression Language)** con el operador `|`.

### Comparación rápida:

```python
# ❌ Antes (clases - deprecado)
from langchain.chains import LLMChain

chain = LLMChain(llm=llm, prompt=prompt)
resultado = chain.run({"input": "hola"})

# ✅ Ahora (LCEL - actual)
from langchain_core.output_parsers import StrOutputParser

chain = prompt | llm | StrOutputParser()
resultado = chain.invoke({"input": "hola"})
```

### Los 5 conceptos clave de LCEL:

#### 1. **Operador `|` (pipe)**
Conecta componentes de izquierda a derecha:
```python
chain = prompt | llm | parser
# El output de prompt → input de llm → input de parser
```

#### 2. **`.invoke()` en vez de `.run()`**
```python
# ✅ Forma actual
resultado = chain.invoke({"input": "texto"})

# También hay .stream() y .batch()
for chunk in chain.stream({"input": "texto"}):
    print(chunk)
```

#### 3. **Runnables: Todo es un Runnable**
Todos los componentes implementan la interfaz `Runnable`:
- PromptTemplate → Runnable
- LLM → Runnable
- Parser → Runnable
- Tu función personalizada → Runnable

Esto permite conectarlos con `|`.

#### 4. **RunnableSequence y RunnableParallel**
```python
# Secuencial (uno después del otro)
chain = step1 | step2 | step3

# Paralelo (todos al mismo tiempo)
from langchain_core.runnables import RunnableParallel

chain = RunnableParallel(
    resumen=prompt1 | llm,
    keywords=prompt2 | llm,
    sentimiento=prompt3 | llm
)
```

#### 5. **Streaming nativo**
```python
# Con LCEL, streaming es automático
for chunk in chain.stream(input):
    print(chunk, end="")
```

### ¿Por qué cambió LangChain a LCEL?

✅ **Más simple**: Menos clases que recordar
✅ **Más rápido**: Ejecución optimizada
✅ **Streaming nativo**: Mejor experiencia de usuario
✅ **Paralelización automática**: Con RunnableParallel
✅ **Mejor debugging**: Integración con LangSmith

### Tabla de equivalencias:

| Antes (Deprecado) | Ahora (LCEL) |
|-------------------|--------------|
| `LLMChain` | `prompt \| llm \| parser` |
| `ConversationChain` | `RunnableWithMessageHistory` |
| `SequentialChain` | `step1 \| step2 \| step3` |
| `SimpleSequentialChain` | `step1 \| step2 \| step3` |
| `.run()` | `.invoke()` |
| `.predict()` | `.invoke()` |
z| `Tool` class | `@tool` decorator |
| `create_react_agent` | `llm.bind_tools()` + custom logic |

### Tu primera chain con LCEL:

```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1. Componentes
llm = ChatOpenAI(model="gpt-4o-mini")
prompt = ChatPromptTemplate.from_template("Explica {concepto} en términos simples")
parser = StrOutputParser()

# 2. Conectar con |
chain = prompt | llm | parser

# 3. Usar
resultado = chain.invoke({"concepto": "inteligencia artificial"})
print(resultado)
```

**Eso es todo. Simple, limpio, poderoso.** 🚀

---

## Conceptos Fundamentales

### 1. **LLM (Large Language Model)**

**¿Qué es?**
Un modelo de IA entrenado con millones de textos que puede entender y generar lenguaje natural.

**Ejemplos:**
- GPT-4o / GPT-4o-mini (OpenAI)
- Claude (Anthropic)
- Llama (Meta)
- Gemini (Google)

**Analogía:**
Es como un empleado muy inteligente que puede escribir, analizar y razonar, pero necesita instrucciones claras.

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",  # El "cerebro"
    temperature=0.7,      # Creatividad (0=robótico, 1=creativo)
)

respuesta = llm.invoke("¿Qué es Python?")
```

### 2. **Prompts**

**¿Qué es?**
Las instrucciones que le das al LLM. La calidad del prompt determina la calidad de la respuesta.

**Prompts malos vs buenos:**

❌ **Malo:**
```python
"Dime sobre productos"
```

✅ **Bueno:**
```python
"""Eres un experto en ventas de equipos de construcción.
Analiza este producto y dame:
1. Características principales
2. Casos de uso
3. Ventajas competitivas

Producto: {producto}
"""
```

**PromptTemplate en LangChain:**
```python
from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate(
    template="""Eres un {rol}.

    Tarea: {tarea}
    Contexto: {contexto}

    Responde de forma {estilo}.""",
    input_variables=["rol", "tarea", "contexto", "estilo"]
)

prompt_final = prompt.format(
    rol="vendedor experto",
    tarea="recomendar un producto",
    contexto="cliente necesita demoler concreto",
    estilo="profesional y concisa"
)
```

### 3. **Embeddings (Vectores)**

**¿Qué es?**
Convertir texto en números (vectores) que las computadoras pueden comparar.

**Analogía:**
Es como darle coordenadas GPS a las palabras. Palabras similares tienen coordenadas cercanas.

```python
"perro" → [0.2, 0.8, 0.1, ...]
"gato"  → [0.3, 0.7, 0.2, ...]  # Similar
"carro" → [0.9, 0.1, 0.8, ...]  # Diferente
```

**En código:**
```python
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# Convertir texto a vector
vector = embeddings.embed_query("rotomartillo para concreto")
# Resultado: [0.123, -0.456, 0.789, ...] (1536 dimensiones)
```

**¿Para qué sirve?**
- Buscar documentos similares
- Comparar textos
- Sistemas de recomendación
- RAG (Retrieval Augmented Generation)

### 4. **Vector Stores (Bases de Datos Vectoriales)**

**¿Qué es?**
Una base de datos especializada en almacenar y buscar vectores (embeddings).

**Analogía:**
Como Google, pero en vez de buscar por palabras exactas, busca por "significado similar".

**Tipos populares:**

| Vector Store | Tipo | Mejor para |
|--------------|------|------------|
| FAISS | Local | Desarrollo, prototipos |
| Pinecone | Cloud | Producción, escala |
| Chroma | Local/Cloud | Balance |
| Weaviate | Cloud | Enterprise |

**Ejemplo:**
```python
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

# 1. Crear documentos
documentos = [
    "El rotomartillo es ideal para concreto",
    "El demoledor es para trabajos pesados",
    "La mezcladora es para preparar concreto"
]

# 2. Convertir a embeddings y almacenar
vectorstore = FAISS.from_texts(
    documentos,
    OpenAIEmbeddings()
)

# 3. Buscar por similitud
resultados = vectorstore.similarity_search("necesito perforar concreto")
# Resultado: ["El rotomartillo es ideal para concreto"]
```

### 5. **RAG (Retrieval Augmented Generation)**

**¿Qué es?**
Un patrón que combina búsqueda + generación para que el LLM responda basándose en tus documentos.

**El problema que resuelve:**
- Los LLMs no conocen tus datos privados
- Los LLMs pueden "alucinar" (inventar información)
- Los LLMs tienen un límite de contexto

**Cómo funciona RAG:**

```
┌─────────────────────────────────────────────────────┐
│  1. Usuario pregunta: "¿Precio del rotomartillo?"  │
└──────────────────┬──────────────────────────────────┘
                   ▼
┌─────────────────────────────────────────────────────┐
│  2. Se convierte la pregunta a embedding (vector)   │
└──────────────────┬──────────────────────────────────┘
                   ▼
┌─────────────────────────────────────────────────────┐
│  3. Se buscan documentos similares en vectorstore   │
│     → "Rotomartillo TE-70: L750 por día"            │
└──────────────────┬──────────────────────────────────┘
                   ▼
┌─────────────────────────────────────────────────────┐
│  4. Se pasa pregunta + documentos al LLM            │
│     Prompt: "Basándote en: [documentos]             │
│              Responde: ¿Precio del rotomartillo?"   │
└──────────────────┬──────────────────────────────────┘
                   ▼
┌─────────────────────────────────────────────────────┐
│  5. LLM genera respuesta basada en los documentos   │
│     → "El Rotomartillo TE-70 cuesta L750 por día"   │
└─────────────────────────────────────────────────────┘
```

**Código completo de RAG:**
```python
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA

# 1. CARGAR documentos
loader = PyPDFLoader("catalogo.pdf")
docs = loader.load()

# 2. DIVIDIR en chunks (pedazos)
splitter = RecursiveCharacterTextSplitter(chunk_size=500)
chunks = splitter.split_documents(docs)

# 3. VECTORIZAR y almacenar
vectorstore = FAISS.from_documents(chunks, OpenAIEmbeddings())

# 4. CREAR sistema RAG
qa = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model="gpt-4o-mini"),
    retriever=vectorstore.as_retriever(search_kwargs={"k": 3})
)

# 5. CONSULTAR
respuesta = qa.invoke({"query": "¿Cuál es el precio del rotomartillo?"})
print(respuesta["result"])
```

---

## Componentes Principales

### 🔗 1. Chains (Cadenas)

**¿Qué son?**
Secuencias de operaciones conectadas. La salida de una operación es la entrada de la siguiente.

**Con LCEL (forma actual):**

#### A) **Chain Básica** (Prompt + LLM + Parser)
```python
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

# Crear componentes
prompt = PromptTemplate(
    template="Traduce '{texto}' a {idioma}",
    input_variables=["texto", "idioma"]
)
llm = ChatOpenAI(model="gpt-4o-mini")
parser = StrOutputParser()

# Conectar con el operador |
chain = prompt | llm | parser

# Invocar
resultado = chain.invoke({"texto": "hello", "idioma": "español"})
# → "hola"
```

#### B) **RunnableSequence** (Cadena Secuencial)
```python
from langchain_core.runnables import RunnablePassthrough

# Chain 1: Generar idea
prompt1 = PromptTemplate(
    template="Dame una idea de negocio sobre: {tema}",
    input_variables=["tema"]
)

# Chain 2: Crear plan (recibe la salida de chain1)
prompt2 = PromptTemplate(
    template="Crea un plan de negocios para esta idea:\n{idea}",
    input_variables=["idea"]
)

# Conectar secuencialmente
chain = (
    {"idea": prompt1 | llm | StrOutputParser()}  # Genera idea
    | prompt2                                      # Usa la idea
    | llm                                          # Genera plan
    | StrOutputParser()
)

resultado = chain.invoke({"tema": "tecnología educativa"})
# → Plan completo de negocio
```

#### C) **RunnableParallel** (Ejecución Paralela)
```python
from langchain_core.runnables import RunnableParallel

# Ejecutar múltiples chains en paralelo
chain = RunnableParallel(
    resumen=prompt_resumen | llm | StrOutputParser(),
    sentimiento=prompt_sentimiento | llm | StrOutputParser(),
    keywords=prompt_keywords | llm | StrOutputParser()
)

resultado = chain.invoke({"texto": "Mi texto aquí..."})
# → {
#     "resumen": "...",
#     "sentimiento": "positivo",
#     "keywords": ["palabra1", "palabra2"]
# }
```

**Cuándo usar Chains:**
- ✅ Flujos predecibles y lineales
- ✅ Procesamiento de datos paso a paso
- ✅ Pipelines de transformación
- ✅ Cuando necesitas ejecutar operaciones en paralelo

**Cuándo NO usar Chains:**
- ❌ Cuando necesitas decisiones dinámicas → Usa Agents
- ❌ Cuando el flujo cambia según el input → Usa LangGraph

---

### 💭 2. Memory (Memoria)

**¿Qué es?**
La capacidad de recordar conversaciones anteriores.

**El problema:**
Por defecto, cada consulta al LLM es independiente. No recuerda nada.

```python
# SIN memoria
llm.invoke("Me llamo Juan")  → "Mucho gusto"
llm.invoke("¿Cuál es mi nombre?")  → "No lo sé" ❌
```

**Con LCEL: RunnableWithMessageHistory**

La forma actual de implementar memoria usa `RunnableWithMessageHistory`:

```python
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

# 1. Crear almacenamiento de mensajes
store = {}

def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

# 2. Crear prompt con placeholder para historial
prompt = ChatPromptTemplate.from_messages([
    ("system", "Eres un asistente útil."),
    MessagesPlaceholder(variable_name="history"),  # Aquí va el historial
    ("human", "{input}")
])

# 3. Crear chain
chain = prompt | ChatOpenAI(model="gpt-4o-mini")

# 4. Agregar memoria
chain_with_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history"
)

# 5. Usar con session_id
config = {"configurable": {"session_id": "user123"}}

chain_with_history.invoke({"input": "Me llamo Juan"}, config=config)
# → "Mucho gusto, Juan"

chain_with_history.invoke({"input": "¿Cuál es mi nombre?"}, config=config)
# → "Tu nombre es Juan" ✅
```

**Ventajas de este enfoque:**
- ✅ Más flexible y modular
- ✅ Soporte para múltiples sesiones simultáneas
- ✅ Compatible con LCEL
- ✅ Fácil de integrar con diferentes backends (Redis, MongoDB, etc.)

**Limitar el historial (ventana deslizante):**

```python
from langchain_core.runnables import RunnableLambda

def limit_messages(messages, k=5):
    """Mantiene solo los últimos k*2 mensajes (k pares user-assistant)"""
    return messages[-(k*2):]

# Agregar antes del LLM
chain = (
    prompt
    | RunnableLambda(lambda x: {
        "input": x["input"],
        "history": limit_messages(x.get("history", []), k=3)
    })
    | ChatOpenAI()
)
```

**Diferentes backends de almacenamiento:**

```python
# Memoria en Redis (persistente)
from langchain_redis import RedisChatMessageHistory

def get_session_history(session_id: str):
    return RedisChatMessageHistory(
        session_id,
        url="redis://localhost:6379"
    )

# Memoria en archivo
from langchain_community.chat_message_histories import FileChatMessageHistory

def get_session_history(session_id: str):
    return FileChatMessageHistory(f"chat_history_{session_id}.json")
```

**Cuándo usar cada estrategia:**

| Estrategia | Tokens | Usar cuando |
|---------|--------|-------------|
| **Historial completo** | Alto | Conversaciones cortas (<10 turnos) |
| **Ventana (k=3-5)** | Medio | Chatbots generales |
| **Resumen con LLM** | Variable | Sesiones muy largas |
| **Backend persistente** | - | Producción, múltiples usuarios |

---

### 🤖 3. Agents (Agentes Autónomos)

**¿Qué son?**
Sistemas que pueden **razonar, decidir y actuar** de forma autónoma.

**Diferencia clave:**
- **Chain**: Sigue un flujo predefinido (rígido)
- **Agent**: Decide qué hacer según la situación (flexible)

**Ejemplo:**

```python
# CHAIN (predefinido)
1. Buscar en catálogo
2. Calcular precio
3. Responder
# Siempre hace los 3 pasos

# AGENT (decide)
Usuario: "¿Tienen rotomartillos?"
Agent: "Solo necesito buscar en catálogo"
       → Ejecuta herramienta de búsqueda
       → Responde
# Solo hace lo necesario
```

**Patrón ReAct (Reason + Act):**

```
Thought: Necesito saber si el producto está disponible
Action: Verificar_Disponibilidad
Action Input: "rotomartillo"
Observation: ✅ Disponible, 5 unidades

Thought: Ahora sé que está disponible, puedo responder
Final Answer: Sí, tenemos 5 rotomartillos disponibles
```

**Código completo de un Agent:**

```python
from langchain.agents import Tool, initialize_agent, AgentType
from langchain.memory import ConversationBufferMemory

# 1. CREAR HERRAMIENTAS
def buscar_producto(nombre: str) -> str:
    """Busca un producto en el catálogo"""
    # Simulación de base de datos
    productos = {
        "rotomartillo": "TE-70, L750/día, disponible",
        "demoledor": "TE-3000, L1100/día, agotado"
    }
    return productos.get(nombre.lower(), "Producto no encontrado")

def calcular_precio(info: str) -> str:
    """Calcula precio total. Input: 'precio_diario,dias' ejemplo: '750,10'"""
    try:
        precio, dias = info.split(',')
        total = float(precio) * int(dias)
        return f"Total: L{total}"
    except:
        return "Error en formato"

tools = [
    Tool(
        name="Buscar_Producto",
        func=buscar_producto,
        description="Busca información de productos. Input: nombre del producto"
    ),
    Tool(
        name="Calcular_Precio",
        func=calcular_precio,
        description="Calcula precio total. Input: 'precio_diario,dias'"
    )
]

# 2. CREAR MEMORIA
memoria = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

# 3. INICIALIZAR AGENTE
agente = initialize_agent(
    tools=tools,
    llm=ChatOpenAI(temperature=0),
    agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memoria,
    verbose=True  # Ver el razonamiento
)

# 4. USAR EL AGENTE
respuesta = agente.run("¿Cuánto cuesta rentar un rotomartillo por 15 días?")

# El agente automáticamente:
# 1. Busca el producto
# 2. Extrae el precio (L750)
# 3. Calcula el total (750 * 15 = 11,250)
# 4. Responde
```

**Tipos de Agents:**

| Tipo | Descripción | Cuándo usar |
|------|-------------|-------------|
| **Zero-shot ReAct** | Decide sin ejemplos previos | Tareas generales |
| **Conversational** | Con memoria | Chatbots |
| **OpenAI Functions** | Usa function calling | Más preciso, solo OpenAI |
| **Structured Chat** | Para múltiples inputs | Tareas complejas |

---

### 🛠️ 4. Tools (Herramientas)

**¿Qué son?**
Funciones que extienden las capacidades del LLM.

**Ejemplos de herramientas:**
- Buscar en Google
- Consultar bases de datos
- Ejecutar código Python
- Llamar APIs
- Hacer cálculos matemáticos
- Leer archivos

**Forma actual: @tool decorator y Function Calling**

```python
from langchain_core.tools import tool

@tool
def buscar_producto(nombre: str) -> str:
    """
    Busca un producto en el catálogo.

    Args:
        nombre: El nombre del producto a buscar

    Returns:
        Información del producto (nombre, precio, disponibilidad)
    """
    productos = {
        "rotomartillo": "TE-70, L750/día, disponible",
        "demoledor": "TE-3000, L1100/día, agotado"
    }
    return productos.get(nombre.lower(), "Producto no encontrado")

@tool
def calcular_precio(precio_diario: float, dias: int) -> str:
    """
    Calcula el precio total de renta.

    Args:
        precio_diario: Precio por día en Lempiras
        dias: Número de días de renta

    Returns:
        Precio total formateado
    """
    total = precio_diario * dias
    return f"Total: L{total:,.2f}"

# Las herramientas están listas para usar
tools = [buscar_producto, calcular_precio]
```

**Usar Tools con Function Calling (OpenAI):**

```python
from langchain_openai import ChatOpenAI

# Vincular tools al LLM
llm = ChatOpenAI(model="gpt-4o-mini")
llm_with_tools = llm.bind_tools(tools)

# El LLM decide cuándo y cómo usar las tools
response = llm_with_tools.invoke("¿Cuánto cuesta rentar un rotomartillo por 5 días?")

# Revisar si el LLM llamó alguna tool
if response.tool_calls:
    for tool_call in response.tool_calls:
        print(f"Tool: {tool_call['name']}")
        print(f"Args: {tool_call['args']}")
```

**⚠️ IMPORTANTE: La descripción**

La descripción es lo MÁS importante. El agente decide qué herramienta usar basándose en ella.

❌ **Mala descripción:**
```python
description="Calcula precios"
```

✅ **Buena descripción:**
```python
description="""Calcula el precio total de renta de equipos.
Input debe ser: 'precio_diario,numero_dias'
Ejemplo: '500,10' para L500/día por 10 días.
Retorna el total con descuentos aplicados."""
```

**Ejemplos de herramientas útiles:**

```python
# 1. HERRAMIENTA DE WIKIPEDIA
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())

# 2. HERRAMIENTA DE BÚSQUEDA WEB
from langchain_community.tools import DuckDuckGoSearchRun

search = DuckDuckGoSearchRun()

# 3. HERRAMIENTA DE PYTHON (ejecutar código)
from langchain_experimental.tools import PythonREPLTool

python_repl = PythonREPLTool()

# 4. HERRAMIENTA PERSONALIZADA
from datetime import datetime

def obtener_fecha(formato: str) -> str:
    """Obtiene la fecha actual. Input: formato ('corto' o 'largo')"""
    if formato == "corto":
        return datetime.now().strftime("%d/%m/%Y")
    else:
        return datetime.now().strftime("%d de %B del %Y")

tool_fecha = Tool(
    name="Obtener_Fecha",
    func=obtener_fecha,
    description="Obtiene la fecha actual. Input: 'corto' o 'largo'"
)
```

---

### 📊 5. Output Parsers (Parsers de Salida)

**¿Qué son?**
Componentes que estructuran las respuestas del LLM en formatos específicos (JSON, listas, objetos).

**El problema:**
Por defecto, el LLM devuelve texto libre. ¿Cómo convertirlo en datos estructurados?

```python
# Sin parser
respuesta = llm.invoke("Dame 3 productos")
# → "1. Rotomartillo\n2. Demoledor\n3. Mezcladora"
# 😕 Difícil de procesar programáticamente
```

**Forma actual: with_structured_output()**

La forma más simple y recomendada es usar `with_structured_output()`:

```python
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from typing import List

# 1. Definir modelo Pydantic
class Producto(BaseModel):
    nombre: str = Field(description="Nombre del producto")
    precio: float = Field(description="Precio por día en Lempiras")
    caracteristicas: List[str] = Field(description="Lista de características")
    disponible: bool = Field(description="Si está disponible")

# 2. Vincular al LLM
llm = ChatOpenAI(model="gpt-4o-mini")
structured_llm = llm.with_structured_output(Producto)

# 3. Usar directamente
producto = structured_llm.invoke("Rotomartillo TE-70, potente, L750/día, en stock")

# Resultado: objeto Pydantic validado ✅
print(producto.nombre)         # "Rotomartillo TE-70"
print(producto.precio)         # 750.0
print(producto.caracteristicas)  # ["potente"]
print(producto.disponible)     # True
```

**Con un chain completo:**

```python
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "Extrae información estructurada del producto."),
    ("human", "{input}")
])

# Chain con salida estructurada
chain = prompt | llm.with_structured_output(Producto)

resultado = chain.invoke({"input": "Demoledor TE-3000, pesado, potente, L1100/día, agotado"})

print(resultado)
# Producto(
#     nombre="Demoledor TE-3000",
#     precio=1100.0,
#     caracteristicas=["pesado", "potente"],
#     disponible=False
# )
```

**Múltiples objetos:**

```python
class Productos(BaseModel):
    productos: List[Producto] = Field(description="Lista de productos")

structured_llm = llm.with_structured_output(Productos)

resultado = structured_llm.invoke(
    "Tenemos: Rotomartillo TE-70 a L750, disponible. Demoledor TE-3000 a L1100, agotado"
)

for producto in resultado.productos:
    print(f"{producto.nombre}: L{producto.precio}")
```

**Alternativa: JsonOutputParser (para JSON simple)**

```python
from langchain_core.output_parsers import JsonOutputParser

parser = JsonOutputParser(pydantic_object=Producto)

prompt = ChatPromptTemplate.from_messages([
    ("system", "Extrae información del producto.\n{format_instructions}"),
    ("human", "{input}")
]).partial(format_instructions=parser.get_format_instructions())

chain = prompt | llm | parser

resultado = chain.invoke({"input": "Rotomartillo TE-70, L750/día"})
# → dict con los campos del modelo
```

#### C) **ListOutputParser** (Listas)

```python
from langchain.output_parsers import CommaSeparatedListOutputParser

parser = CommaSeparatedListOutputParser()

prompt = PromptTemplate(
    template="""Lista 5 equipos de construcción.

{format_instructions}
""",
    input_variables=[],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

chain = prompt | llm | parser

resultado = chain.invoke({})
print(resultado)
# ['Rotomartillo', 'Demoledor', 'Mezcladora', 'Compactador', 'Allanadora']
```

**Cuándo usar cada método:**

| Método | Usar cuando | Ventaja |
|--------|-------------|---------|
| **with_structured_output()** | Siempre que sea posible | Más simple, integrado |
| **JsonOutputParser** | Necesitas más control | Flexible, personalizable |
| **PydanticOutputParser** | Validación compleja | Validadores personalizados |
| **StrOutputParser** | Solo texto plano | Muy rápido |

---

## Guía de Estudio por Niveles

### 🟢 Nivel 1: Fundamentos (Semana 1-2)

**Objetivos:**
- ✅ Entender qué es un LLM
- ✅ Hacer tu primera llamada a OpenAI
- ✅ Crear prompts básicos
- ✅ Usar PromptTemplates

**Práctica:**
```python
# Ejercicio 1: Primera llamada
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")
respuesta = llm.invoke("¿Qué es Python?")
print(respuesta.content)

# Ejercicio 2: Prompt Template
from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate(
    template="Explica {concepto} a un niño de 10 años",
    input_variables=["concepto"]
)

chain = prompt | llm
respuesta = chain.invoke({"concepto": "inteligencia artificial"})
```

**Recursos:**
- [LangChain Quickstart](https://python.langchain.com/docs/get_started/quickstart)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)

---

### 🟡 Nivel 2: Componentes Básicos (Semana 3-4)

**Objetivos:**
- ✅ Entender embeddings
- ✅ Crear tu primer sistema RAG
- ✅ Usar vector stores
- ✅ Trabajar con documentos

**Práctica:**
```python
# Ejercicio: Sistema RAG básico
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA

# 1. Cargar documento
loader = TextLoader("mi_documento.txt")
docs = loader.load()

# 2. Dividir
splitter = CharacterTextSplitter(chunk_size=1000)
chunks = splitter.split_documents(docs)

# 3. Vectorizar
vectorstore = FAISS.from_documents(chunks, OpenAIEmbeddings())

# 4. Crear RAG
qa = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(),
    retriever=vectorstore.as_retriever()
)

# 5. Consultar
respuesta = qa.invoke({"query": "¿De qué trata el documento?"})
```

**Conceptos clave:**
- Document Loaders (PDF, TXT, CSV, etc.)
- Text Splitters (Character, Recursive, Token)
- Embeddings (OpenAI, HuggingFace)
- Vector Stores (FAISS, Chroma)

---

### 🟠 Nivel 3: Chains y Memory (Semana 5-6)

**Objetivos:**
- ✅ Crear chains secuenciales
- ✅ Implementar memoria conversacional
- ✅ Combinar múltiples chains

**Práctica:**
```python
# Ejercicio: Chatbot con memoria
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferWindowMemory

memoria = ConversationBufferWindowMemory(k=5)

conversacion = ConversationChain(
    llm=ChatOpenAI(),
    memory=memoria
)

# Simular conversación
conversacion.predict(input="Hola, me llamo Ana")
conversacion.predict(input="Estudio ingeniería")
conversacion.predict(input="¿Recuerdas mi nombre?")
# → "Sí, eres Ana"
```

**Conceptos clave:**
- LLMChain
- SequentialChain
- RouterChain
- ConversationBufferMemory
- ConversationSummaryMemory

---

### 🔴 Nivel 4: Agents y Tools (Semana 7-8)

**Objetivos:**
- ✅ Crear herramientas personalizadas
- ✅ Construir agentes autónomos
- ✅ Entender el patrón ReAct

**Práctica:**
```python
# Ejercicio: Agente con herramientas
from langchain.agents import Tool, initialize_agent, AgentType

# Herramienta personalizada
def calculadora(operacion: str) -> str:
    """Calcula operaciones. Input: 'num1,operador,num2' ej: '5,+,3'"""
    try:
        num1, op, num2 = operacion.split(',')
        num1, num2 = float(num1), float(num2)

        if op == '+': return str(num1 + num2)
        elif op == '-': return str(num1 - num2)
        elif op == '*': return str(num1 * num2)
        elif op == '/': return str(num1 / num2)
    except:
        return "Error en formato"

tools = [
    Tool(
        name="Calculadora",
        func=calculadora,
        description="Realiza operaciones matemáticas. Input: 'num1,operador,num2'"
    )
]

agente = initialize_agent(
    tools=tools,
    llm=ChatOpenAI(temperature=0),
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

agente.run("¿Cuánto es 25 multiplicado por 4?")
```

**Conceptos clave:**
- Tool creation
- Agent types
- ReAct pattern
- Agent memory
- Error handling

---

### ⚫ Nivel 5: Avanzado (Semana 9+)

**Objetivos:**
- ✅ Output parsers complejos
- ✅ Multi-agent systems
- ✅ LangGraph (workflows)
- ✅ Production deployment

**Temas avanzados:**
- Custom retrievers
- Hybrid search (vector + keyword)
- Streaming responses
- Async operations
- Cost optimization
- Monitoring con LangSmith

---

## Patrones y Mejores Prácticas

### ✅ DO's (Haz esto)

#### 1. **Usa LCEL en vez de clases legacy**
```python
# ✅ LCEL (actual)
chain = prompt | llm | StrOutputParser()

# En vez de usar clases deprecadas
```

#### 2. **Usa temperature adecuada**
```python
# Para tareas creativas (escritura, ideas)
llm = ChatOpenAI(temperature=0.8)

# Para tareas precisas (análisis, clasificación)
llm = ChatOpenAI(temperature=0.1)
```

#### 3. **Cachea vectorstores**
```python
# Guardar (primera vez)
vectorstore.save_local("mi_vectorstore")

# Cargar (siguientes veces) - ahorra dinero
vectorstore = FAISS.load_local("mi_vectorstore", embeddings)
```

#### 4. **Usa RecursiveCharacterTextSplitter**
```python
# ✅ RecursiveCharacterTextSplitter (respeta contexto)
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
    separators=["\n\n", "\n", ". ", " "]  # Prioriza divisiones naturales
)
```

#### 5. **Valida inputs en Tools**
```python
from langchain_core.tools import tool

@tool
def mi_herramienta(input: str) -> str:
    """Descripción de la herramienta"""
    # ✅ Siempre valida
    if not input or len(input) == 0:
        return "Error: Input vacío"

    # ✅ Maneja excepciones
    try:
        resultado = procesar(input)
        return resultado
    except Exception as e:
        return f"Error: {str(e)}"
```

#### 6. **Usa RunnableParallel para paralelizar**
```python
from langchain_core.runnables import RunnableParallel

# ✅ Ejecuta múltiples chains en paralelo
chain = RunnableParallel(
    resumen=prompt_resumen | llm,
    sentimiento=prompt_sentimiento | llm,
    keywords=prompt_keywords | llm
)
# Más rápido que ejecutar uno por uno
```

#### 7. **Streaming para mejor UX**
```python
# ✅ Streaming de respuestas
chain = prompt | llm | StrOutputParser()

for chunk in chain.stream({"input": "Explica IA"}):
    print(chunk, end="", flush=True)
# El usuario ve la respuesta en tiempo real
```

#### 8. **Usa with_structured_output() para datos estructurados**
```python
# ✅ Forma simple y directa
structured_llm = llm.with_structured_output(MiModelo)
resultado = structured_llm.invoke("input")
```

---

### ❌ DON'Ts (Evita esto)

#### 1. **No uses Buffer Memory para todo**
```python
# ❌ En conversaciones largas
memoria = ConversationBufferMemory()  # Consumirá MUCHOS tokens

# ✅ Usa Window o Summary
memoria = ConversationBufferWindowMemory(k=5)
```

#### 2. **No ignores el chunk_overlap**
```python
# ❌ Sin overlap (puede cortar información importante)
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)

# ✅ Con overlap (mantiene contexto)
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
```

#### 3. **No uses descripciones vagas en Tools**
```python
# ❌ Vago
Tool(name="Buscar", func=buscar, description="Busca cosas")

# ✅ Específico
Tool(
    name="Buscar_Productos",
    func=buscar,
    description="Busca productos en el catálogo. Input: nombre o categoría del producto. Retorna: nombre, precio, disponibilidad"
)
```

#### 4. **No confíes ciegamente en el agente**
```python
# ❌ Sin validación
resultado = agente.run(input_usuario)
ejecutar_accion_critica(resultado)

# ✅ Con validación
resultado = agente.run(input_usuario)
if validar(resultado):
    ejecutar_accion_critica(resultado)
else:
    manejar_error()
```

#### 5. **No uses temperature alta para tareas críticas**
```python
# ❌ Para análisis financiero, clasificación, etc.
llm = ChatOpenAI(temperature=0.9)

# ✅ Usa temperature baja
llm = ChatOpenAI(temperature=0.1)
```

---

## Troubleshooting Común

### 🐛 Problema 1: "El agente no usa la herramienta correcta"

**Causa:** Descripción de la herramienta es vaga o confusa

**Solución:**
```python
# ❌ Antes
Tool(name="Calcular", func=calc, description="Calcula")

# ✅ Después
Tool(
    name="Calcular_Precio",
    func=calc,
    description="""Calcula el precio total de renta.
    Input: 'precio_diario,numero_dias' (ejemplo: '500,10')
    Output: Total en Lempiras con descuentos aplicados
    Usar SOLO para cálculos de precios, no para otras operaciones matemáticas."""
)
```

---

### 🐛 Problema 2: "RateLimitError de OpenAI"

**Causa:** Demasiadas llamadas a la API

**Soluciones:**
1. Cachear resultados
2. Usar modelos más baratos para tareas simples
3. Implementar retry logic

```python
from langchain_openai import ChatOpenAI
import time

llm = ChatOpenAI(
    model="gpt-4o-mini",  # Más barato que gpt-4
    request_timeout=60,
    max_retries=3  # Reintenta automáticamente
)
```

---

### 🐛 Problema 3: "El agente entra en loop infinito"

**Causa:** No limitar iteraciones

**Solución:**
```python
agente = initialize_agent(
    tools=tools,
    llm=llm,
    max_iterations=5,  # ✅ Máximo 5 intentos
    early_stopping_method="generate"  # ✅ Para si no progresa
)
```

---

### 🐛 Problema 4: "Vectorstore muy lento al buscar"

**Causa:** Demasiados documentos o chunks muy grandes

**Soluciones:**
```python
# 1. Reducir k (número de documentos recuperados)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})  # En vez de 10

# 2. Usar chunks más pequeños
splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,  # En vez de 1000
    chunk_overlap=30
)

# 3. Filtrar por metadata
retriever = vectorstore.as_retriever(
    search_kwargs={
        "k": 5,
        "filter": {"categoria": "equipos"}  # Solo busca en "equipos"
    }
)
```

---

### 🐛 Problema 5: "Output parser falla con errores de formato"

**Causa:** El LLM no sigue el formato exacto

**Solución:**
```python
from langchain.output_parsers import OutputFixingParser

# Parser original
parser = PydanticOutputParser(pydantic_object=Producto)

# Wrapper que intenta arreglar errores automáticamente
fixing_parser = OutputFixingParser.from_llm(
    parser=parser,
    llm=ChatOpenAI()
)

chain = prompt | llm | fixing_parser  # ✅ Más robusto
```

---

### 🐛 Problema 6: "Memory consume demasiados tokens"

**Causa:** Usar ConversationBufferMemory en conversaciones largas

**Solución:**
```python
# ❌ Antes (puede llegar a 10k+ tokens)
memoria = ConversationBufferMemory()

# ✅ Opción 1: Window
memoria = ConversationBufferWindowMemory(k=5)  # ~1k tokens

# ✅ Opción 2: Summary
memoria = ConversationSummaryMemory(llm=llm)  # ~500 tokens
```

---

## Recursos de Aprendizaje

### 📚 Documentación Oficial
- [LangChain Docs](https://python.langchain.com/docs/get_started/introduction) - Documentación oficial
- [LangChain API Reference](https://api.python.langchain.com/en/latest/) - Referencia completa
- [LangChain GitHub](https://github.com/langchain-ai/langchain) - Código fuente

### 🎓 Cursos Recomendados

#### Gratis:
1. **[LangChain Crash Course - FreeCodeCamp](https://www.youtube.com/watch?v=LbT1yp6quS8)**
   - Duración: 2 horas
   - Nivel: Principiante

2. **[LangChain Official Tutorials](https://python.langchain.com/docs/tutorials/)**
   - Tutoriales paso a paso

#### De pago:
1. **[Functions, Tools and Agents with LangChain - DeepLearning.AI](https://www.deeplearning.ai/short-courses/functions-tools-agents-langchain/)**
   - Instructor: Harrison Chase (creador de LangChain)
   - Duración: ~2 horas
   - Costo: Gratis con certificado opcional

2. **[LangChain for LLM Application Development - Coursera](https://www.coursera.org/learn/langchain-for-llm-application-development)**
   - Certificación profesional

### 📖 Libros
- **"Build LLM Apps with LangChain"** - Conceptos y patrones
- **"Generative AI with LangChain"** - Packt Publishing

### 🎥 Canales de YouTube
- [LangChain Official](https://www.youtube.com/@LangChain)
- [Sam Witteveen](https://www.youtube.com/@samwitteveenai) - Tutoriales avanzados
- [Prompt Engineering](https://www.youtube.com/@engineerprompt)

### 💬 Comunidad
- [LangChain Discord](https://discord.gg/langchain)
- [r/LangChain](https://www.reddit.com/r/LangChain/)
- [LangChain Twitter](https://twitter.com/LangChainAI)

### 📊 Herramientas Complementarias
- **[LangSmith](https://www.langchain.com/langsmith)** - Debugging y monitoring
- **[LangServe](https://github.com/langchain-ai/langserve)** - Deploy de chains como APIs
- **[LangGraph](https://github.com/langchain-ai/langgraph)** - Workflows complejos

---

## 🗺️ Roadmap de Aprendizaje

### Mes 1: Fundamentos
- ✅ Semana 1: LLMs, prompts, OpenAI API
- ✅ Semana 2: PromptTemplates, LCEL, chains básicas
- ✅ Semana 3: Embeddings, vector stores
- ✅ Semana 4: Sistema RAG completo

### Mes 2: Componentes Avanzados
- ✅ Semana 5: RunnableSequence, RunnableParallel
- ✅ Semana 6: Memory con RunnableWithMessageHistory
- ✅ Semana 7: Tools con @tool decorator
- ✅ Semana 8: Function Calling, bind_tools()

### Mes 3: Proyectos Reales
- ✅ Semana 9: Output parsers, with_structured_output()
- ✅ Semana 10: Proyecto: Chatbot con RAG + Memory
- ✅ Semana 11: Introducción a LangGraph
- ✅ Semana 12: Optimización, deployment

### Después:
- LangGraph avanzado (workflows con loops, condicionales)
- Multi-agent systems con LangGraph
- Production best practices
- Monitoring con LangSmith

---

## 🔀 LangGraph: Workflows Complejos

### ¿Qué es LangGraph?

**LangGraph** es una extensión de LangChain para construir **workflows con estado** que pueden tener:
- ✅ **Loops** (ciclos)
- ✅ **Condicionales** (if/else)
- ✅ **Estado persistente**
- ✅ **Múltiples agentes interactuando**

### ¿Cuándo usar LangGraph?

| Usa LangChain (LCEL) | Usa LangGraph |
|---------------------|---------------|
| Flujos lineales | Flujos con loops |
| Sin condicionales complejos | Decisiones dinámicas |
| Single-agent | Multi-agent |
| No necesitas loops | Auto-corrección, reintentos |

### Ejemplo: Agente que se auto-corrige

**Problema que resuelve:** Un agente que verifica sus propias respuestas y reintenta si hay errores.

```python
from typing import TypedDict
from langgraph.graph import StateGraph, END

# 1. Definir el estado
class State(TypedDict):
    pregunta: str
    respuesta: str
    verificado: bool
    intentos: int

# 2. Definir nodos (funciones)
def resolver(state: State) -> State:
    """Resuelve el problema"""
    # Lógica para resolver
    respuesta = llm.invoke(state["pregunta"])
    return {
        **state,
        "respuesta": respuesta,
        "intentos": state["intentos"] + 1
    }

def verificar(state: State) -> State:
    """Verifica si la respuesta es correcta"""
    verificacion = llm.invoke(f"¿Es correcta esta respuesta? {state['respuesta']}")
    return {
        **state,
        "verificado": "sí" in verificacion.lower()
    }

# 3. Función de decisión (edge condicional)
def decidir_siguiente(state: State) -> str:
    if state["verificado"]:
        return "finalizar"
    elif state["intentos"] < 3:
        return "reintentar"
    else:
        return "pedir_ayuda"

# 4. Construir el grafo
workflow = StateGraph(State)

# Agregar nodos
workflow.add_node("resolver", resolver)
workflow.add_node("verificar", verificar)
workflow.add_node("pedir_ayuda", lambda s: {**s, "respuesta": "Necesito ayuda humana"})

# Agregar edges (conexiones)
workflow.set_entry_point("resolver")
workflow.add_edge("resolver", "verificar")

# Edge condicional (aquí está el loop!)
workflow.add_conditional_edges(
    "verificar",
    decidir_siguiente,
    {
        "reintentar": "resolver",  # LOOP: vuelve a resolver
        "pedir_ayuda": "pedir_ayuda",
        "finalizar": END
    }
)
workflow.add_edge("pedir_ayuda", END)

# 5. Compilar y ejecutar
app = workflow.compile()

# Ejecutar
resultado = app.invoke({
    "pregunta": "¿Cuánto es 234 * 567?",
    "respuesta": "",
    "verificado": False,
    "intentos": 0
})

print(resultado["respuesta"])
```

**Lo que hace este código:**
1. Resuelve el problema
2. Verifica la respuesta
3. Si está mal, **vuelve a intentar** (loop) hasta 3 veces
4. Si sigue mal, pide ayuda humana

**Esto es IMPOSIBLE con chains normales** porque no pueden hacer loops.

### Ventajas de LangGraph

✅ **Estado persistente**: El estado se mantiene entre nodos
✅ **Loops**: Puedes volver atrás en el workflow
✅ **Condicionales**: Decisiones basadas en el estado
✅ **Visualizable**: Puedes ver el grafo visualmente
✅ **Checkpointing**: Guardar y reanudar workflows

### Cuándo profundizar en LangGraph

Aprende LangGraph cuando:
- ✅ Ya dominas LCEL y chains básicas
- ✅ Necesitas workflows con auto-corrección
- ✅ Necesitas múltiples agentes coordinados
- ✅ Necesitas loops o condicionales complejos

---

## 💡 Consejos Finales para tu Estudio

### 1. **Aprende haciendo**
No solo leas la documentación. Escribe código todos los días.

### 2. **Empieza simple**
No intentes crear un sistema complejo en el día 1. Construye paso a paso.

### 3. **Lee código de otros**
Explora el [LangChain Cookbook](https://github.com/langchain-ai/langchain/tree/master/cookbook)

### 4. **Experimenta con diferentes modelos**
```python
# Prueba diferentes modelos para diferentes tareas
gpt4 = ChatOpenAI(model="gpt-4")  # Tareas complejas
gpt4_mini = ChatOpenAI(model="gpt-4o-mini")  # Tareas simples
```

### 5. **Tracking de costos**
Siempre monitorea cuánto gastas:
```python
with get_openai_callback() as cb:
    resultado = chain.invoke(input)
    print(f"Costo: ${cb.total_cost}")
```

### 6. **Únete a la comunidad**
- Haz preguntas en Discord
- Lee issues en GitHub
- Sigue a expertos en Twitter

### 7. **Construye proyectos personales**
Las mejores ideas de proyecto:
- Chatbot para tu área de expertise
- Sistema RAG sobre tus documentos
- Agente para automatizar tareas repetitivas
- Analizador de datos con agents

---

## 🎯 Tu Primer Proyecto Completo

**Sistema de Atención al Cliente con IA**

### Características:
1. ✅ RAG sobre catálogo de productos
2. ✅ Memoria conversacional
3. ✅ Agente con herramientas:
   - Buscar productos
   - Verificar disponibilidad
   - Calcular precios
4. ✅ Output estructurado
5. ✅ Tracking de costos

### Código base:
```python
# Ver el notebook: LangChain_Avanzado_Clase2.ipynb
# Sección: "Proyecto Final - Agente Completo de Ventas"
```

---

## ✅ Checklist de Dominio de LangChain

Marca cuando domines cada concepto:

### Fundamentos
- [ ] Entiendo qué es un LLM
- [ ] Puedo crear prompts efectivos
- [ ] Sé usar PromptTemplate y ChatPromptTemplate
- [ ] Entiendo qué es LCEL
- [ ] Puedo usar el operador `|` para conectar componentes
- [ ] Entiendo qué son los embeddings
- [ ] Puedo crear un vector store

### RAG
- [ ] Puedo cargar documentos (PDF, TXT)
- [ ] Sé dividir documentos en chunks
- [ ] Entiendo la búsqueda por similitud
- [ ] Puedo crear un sistema RAG completo
- [ ] Sé optimizar el retrieval

### Chains con LCEL
- [ ] Puedo crear chains básicas: prompt | llm | parser
- [ ] Entiendo RunnableSequence
- [ ] Entiendo RunnableParallel
- [ ] Puedo combinar múltiples chains
- [ ] Sé cuándo usar chains vs agents vs LangGraph

### Memory
- [ ] Entiendo RunnableWithMessageHistory
- [ ] Puedo implementar memoria conversacional
- [ ] Sé manejar múltiples sesiones
- [ ] Entiendo trade-offs de tokens
- [ ] Puedo limitar el historial (ventana deslizante)

### Tools
- [ ] Puedo crear tools con @tool decorator
- [ ] Entiendo Function Calling
- [ ] Sé usar bind_tools()
- [ ] Puedo crear herramientas personalizadas
- [ ] Entiendo cómo el LLM decide qué tool usar

### Output Parsers
- [ ] Puedo usar with_structured_output()
- [ ] Entiendo JsonOutputParser
- [ ] Sé validar outputs con Pydantic
- [ ] Puedo manejar errores de parsing

### LangGraph (Avanzado)
- [ ] Entiendo qué es StateGraph
- [ ] Puedo crear nodos y edges
- [ ] Entiendo conditional edges
- [ ] Sé implementar loops
- [ ] Sé cuándo usar LangGraph vs chains

### Producción
- [ ] Sé optimizar costos
- [ ] Entiendo caching
- [ ] Puedo implementar streaming
- [ ] Puedo manejar errores
- [ ] Sé monitorear performance

---

## 🚀 ¡Siguiente Paso!

### Notebooks para practicar:

1. **`LangChain_LCEL_Moderno.ipynb`** ⭐ EMPIEZA AQUÍ
   - Sintaxis LCEL actual
   - Chains, Memory, Tools, Output Parsers, RAG
   - Todo con las mejores prácticas actuales

2. **`LangGraph_Demo_Simple.ipynb`**
   - Ejemplo de auto-corrección con loops
   - Introducción a LangGraph
   - Ver cuando LCEL no es suficiente

### Plan de estudio:

1. **Lee esta guía completa** 📖
2. **Ejecuta `LangChain_LCEL_Moderno.ipynb` celda por celda**
3. **Experimenta**: Cambia parámetros, prueba cosas nuevas
4. **Construye tu propio proyecto**: Chatbot con RAG + Memory
5. **Cuando domines LCEL**: Explora `LangGraph_Demo_Simple.ipynb`

**¡Éxito en tu aprendizaje! 🎓**

---

## 📞 ¿Preguntas?

Si algo no queda claro:
1. Busca en la [documentación oficial](https://python.langchain.com/)
2. Pregunta en [Discord de LangChain](https://discord.gg/langchain)
3. Revisa ejemplos en [GitHub](https://github.com/langchain-ai/langchain)

**Recuerda:** La mejor forma de aprender es construyendo. ¡Manos a la obra! 💪
