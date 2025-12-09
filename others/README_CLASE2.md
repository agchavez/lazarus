# 🎓 Clase 2 - LangChain Avanzado: Agentes y Herramientas

## 📋 Resumen de la Clase

Esta clase profundiza en LangChain, explorando conceptos avanzados que permiten crear sistemas de IA más sofisticados y autónomos.

---

## 🎯 Objetivos de Aprendizaje

Al finalizar esta clase, los estudiantes podrán:

1. ✅ Crear y componer **Chains** (cadenas) complejas
2. ✅ Implementar **Memory** (memoria) conversacional en diferentes modalidades
3. ✅ Construir **Agents** (agentes) autónomos que razonan y actúan
4. ✅ Desarrollar **Tools** (herramientas) personalizadas
5. ✅ Estructurar salidas con **Output Parsers**
6. ✅ Integrar todos los componentes en un sistema completo

---

## 📚 Contenido de la Clase

### **Parte 1: Chains (Cadenas)** - 20 minutos

#### Conceptos clave:
- **LLMChain**: Cadena básica (prompt + LLM)
- **SequentialChain**: Encadena múltiples operaciones
- **SimpleSequentialChain**: Versión simplificada
- **RouterChain**: Enruta a diferentes chains según entrada

#### Ejemplo práctico:
```python
# Chain 1: Genera características técnicas
# Chain 2: Convierte a pitch de ventas
# Resultado: Pipeline automatizado de marketing
```

#### ¿Por qué es importante?
- Permite crear workflows complejos
- Reutilización de componentes
- Código más limpio y mantenible

---

### **Parte 2: Memory (Memoria)** - 25 minutos

#### Tipos de memoria:

1. **ConversationBufferMemory**
   - Almacena TODO el historial
   - Ideal para conversaciones cortas
   - ⚠️ Puede consumir muchos tokens

2. **ConversationBufferWindowMemory**
   - Solo recuerda las últimas K interacciones
   - Eficiente en tokens
   - Pierde contexto antiguo

3. **ConversationSummaryMemory**
   - Resume conversaciones largas
   - Balance entre contexto y eficiencia
   - Usa LLM para generar resúmenes

4. **ConversationEntityMemory**
   - Recuerda entidades mencionadas (personas, lugares, productos)
   - Ideal para CRM y atención al cliente

#### Comparación:

| Tipo | Tokens usados | Contexto | Mejor para |
|------|--------------|----------|------------|
| Buffer | Alto | Completo | Conversaciones cortas |
| Window | Medio | Parcial | Chatbots generales |
| Summary | Bajo | Resumido | Sesiones largas |
| Entity | Bajo | Específico | CRM, ventas |

#### Ejercicio práctico:
- Crear un chatbot que recuerde el nombre del cliente
- Probar las 3 modalidades de memoria
- Analizar cuándo usar cada una

---

### **Parte 3: Agents (Agentes Autónomos)** - 30 minutos

#### ¿Qué es un agente?
Un agente es un sistema que puede:
- **Razonar**: Analiza el problema
- **Decidir**: Elige qué herramienta usar
- **Actuar**: Ejecuta acciones
- **Observar**: Evalúa resultados
- **Repetir**: Itera hasta resolver

#### Patrón ReAct (Reason + Act):
```
Thought: Necesito verificar si el producto está disponible
Action: Verificar_Disponibilidad
Action Input: "rotomartillo"
Observation: ✅ Disponible, 5 unidades en stock
Thought: Ahora puedo responder al cliente
Final Answer: Sí, tenemos rotomartillos disponibles...
```

#### Tipos de agentes en LangChain:

1. **Zero-shot React**
   - Decide herramientas sin ejemplos previos
   - Más flexible

2. **Conversational React**
   - Con memoria conversacional
   - Ideal para chatbots

3. **OpenAI Functions**
   - Usa function calling de OpenAI
   - Más preciso y rápido

#### Ejercicio:
- Crear agente con 3 herramientas personalizadas
- Observar cómo razona y decide
- Analizar el patrón ReAct en acción

---

### **Parte 4: Tools (Herramientas)** - 20 minutos

#### ¿Qué son las herramientas?
Funciones que extienden las capacidades del LLM:
- Cálculos matemáticos
- Consultas a bases de datos
- APIs externas
- Búsquedas web
- Verificaciones de inventario

#### Anatomía de una herramienta:

```python
Tool(
    name="Nombre_Herramienta",
    func=mi_funcion,
    description="Descripción clara de qué hace y cómo usarla"
)
```

⚠️ **Importante**: La descripción es CRÍTICA. El agente decide qué herramienta usar basándose en ella.

#### Ejemplos de herramientas:

1. **Calcular_Descuento**
   - Input: "precio,dias"
   - Output: Total con descuentos

2. **Verificar_Disponibilidad**
   - Input: nombre del equipo
   - Output: Stock disponible

3. **Buscar_Catalogo**
   - Input: descripción del producto
   - Output: Productos similares (RAG)

#### Ejercicio:
- Crear 2 herramientas personalizadas
- Integrarlas en un agente
- Probar con diferentes consultas

---

### **Parte 5: Output Parsers** - 15 minutos

#### ¿Por qué estructurar salidas?
- Poder procesar respuestas programáticamente
- Validar tipos de datos
- Integrar con sistemas externos

#### Tipos de parsers:

1. **StructuredOutputParser**
   ```python
   # Define esquema
   schemas = [
       ResponseSchema(name="precio", description="Precio en Lempiras"),
       ResponseSchema(name="disponible", description="Si está disponible")
   ]
   # Retorna: {"precio": "500", "disponible": "Sí"}
   ```

2. **PydanticOutputParser**
   ```python
   class Producto(BaseModel):
       nombre: str
       precio: float
       disponible: bool
   # Retorna objeto validado con tipos correctos
   ```

3. **ListOutputParser**
   - Para listas
   - Ejemplo: Lista de recomendaciones

#### ¿Cuándo usar cada uno?

| Parser | Usar cuando | Ventajas |
|--------|------------|----------|
| Structured | Necesitas JSON simple | Fácil de usar |
| Pydantic | Necesitas validación de tipos | Robusto, type-safe |
| List | Necesitas listas | Simple para arrays |

---

### **Parte 6: Proyecto Integrador** - 30 minutos

#### Sistema completo de ventas que integra:

```
┌─────────────────────────────────────────┐
│         AGENTE DE VENTAS                │
│                                         │
│  ┌─────────────────────────────────┐   │
│  │   MEMORIA CONVERSACIONAL        │   │
│  │   (Recuerda cliente y contexto) │   │
│  └─────────────────────────────────┘   │
│                                         │
│  ┌─────────────────────────────────┐   │
│  │   HERRAMIENTAS:                 │   │
│  │   • Buscar_Catalogo (RAG)       │   │
│  │   • Verificar_Disponibilidad    │   │
│  │   • Calcular_Descuento          │   │
│  │   • Calcular_Fecha_Entrega      │   │
│  └─────────────────────────────────┘   │
│                                         │
│  ┌─────────────────────────────────┐   │
│  │   RAZONAMIENTO ReAct            │   │
│  │   (Decide qué hacer)            │   │
│  └─────────────────────────────────┘   │
└─────────────────────────────────────────┘
```

#### Flujo de una venta:
1. Cliente: "Necesito demoler concreto"
2. Agente busca en catálogo (RAG)
3. Agente recomienda productos
4. Cliente: "¿Cuánto por 20 días?"
5. Agente calcula con descuentos
6. Cliente: "¿Está disponible?"
7. Agente verifica inventario
8. ✅ Venta completada

---

## 🆚 Diferencias con la Clase 1

| Aspecto | Clase 1 | Clase 2 |
|---------|---------|---------|
| **Enfoque** | RAG básico con OpenAI | LangChain avanzado |
| **Componentes** | Retrieval + Generation | Agents + Memory + Tools |
| **Complejidad** | Lineal (pregunta → respuesta) | Autónomo (razonamiento) |
| **Memoria** | Sin memoria | Memoria conversacional |
| **Herramientas** | Solo RAG | Múltiples tools personalizadas |
| **Decisiones** | Predefinidas | Agente decide |
| **Estructuración** | Texto libre | Output parsers (JSON, Pydantic) |

---

## 💡 Casos de Uso Reales

### 1. **Customer Support Bot**
- Memoria: Recuerda historial del cliente
- Tools: Consulta tickets, base de conocimiento
- Output: Respuestas estructuradas para CRM

### 2. **Research Assistant**
- Memoria: Mantiene contexto de investigación
- Tools: Wikipedia, búsqueda web, PDF
- Output: Informes estructurados

### 3. **Sales Agent**
- Memoria: Perfil del cliente
- Tools: Catálogo, inventario, descuentos
- Output: Propuestas de venta

### 4. **Code Assistant**
- Memoria: Contexto del proyecto
- Tools: Ejecutar código, buscar docs
- Output: Código validado

---

## 🛠️ Stack Tecnológico

```
Capa de Presentación
    ↓
LangChain Agents (Razonamiento)
    ↓
Memory (Contexto) + Tools (Acciones)
    ↓
LLM (OpenAI GPT-4o-mini)
    ↓
Vectorstore (FAISS) + Embeddings
    ↓
Datos (PDF, APIs, Bases de datos)
```

---

## 📊 Plan de Clase (140 minutos)

| Tiempo | Actividad | Tipo |
|--------|-----------|------|
| 0-10 min | Repaso Clase 1 + Intro | Teoría |
| 10-30 min | **Chains** (demo + ejercicio) | Práctica |
| 30-55 min | **Memory** (3 tipos + comparación) | Práctica |
| 55-60 min | Break | - |
| 60-90 min | **Agents + Tools** (demo completo) | Práctica |
| 90-105 min | **Output Parsers** | Práctica |
| 105-135 min | **Proyecto Integrador** | Práctica |
| 135-140 min | Q&A + Ejercicio final | Discusión |

---

## 🎯 Ejercicios Propuestos

### Ejercicio 1: Chain Composer (15 min)
Crea una cadena que:
1. Recibe descripción de un proyecto
2. Genera lista de equipos necesarios
3. Calcula presupuesto total

### Ejercicio 2: Memory Comparison (15 min)
- Implementa los 3 tipos de memoria
- Prueba con una conversación de 10 turnos
- Compara tokens usados y contexto mantenido

### Ejercicio 3: Custom Agent (30 min)
Crea un agente para:
- Gestionar proyectos de construcción
- Herramientas: calcular materiales, asignar equipos, estimar tiempo
- Con memoria de proyectos anteriores

---

## 📖 Recursos Adicionales

### Documentación oficial:
- [LangChain Docs](https://python.langchain.com/docs/get_started/introduction)
- [LangChain Agents](https://python.langchain.com/docs/modules/agents/)
- [LangChain Memory](https://python.langchain.com/docs/modules/memory/)
- [LangChain Tools](https://python.langchain.com/docs/modules/tools/)

### Tutoriales recomendados:
- [Building Agents with LangChain](https://www.deeplearning.ai/short-courses/functions-tools-agents-langchain/)
- [LangChain Cookbook](https://github.com/langchain-ai/langchain/tree/master/cookbook)

### Videos:
- [LangChain Crash Course](https://www.youtube.com/watch?v=LbT1yp6quS8)
- [Building Production-Ready Agents](https://www.youtube.com/watch?v=DWUdGhRrv2c)

---

## 🚀 Próximos Pasos

### Después de esta clase, puedes:
1. ✅ Construir agentes autónomos complejos
2. ✅ Integrar múltiples fuentes de datos
3. ✅ Crear sistemas de IA conversacionales
4. ✅ Estructurar salidas para sistemas empresariales

### Temas para Clase 3 (opcional):
- **LangGraph**: Workflows complejos con grafos
- **LangSmith**: Monitoring y debugging
- **Vector Databases avanzadas**: Pinecone, Weaviate
- **Multi-agent systems**: Varios agentes colaborando
- **Production deployment**: Escalabilidad y optimización

---

## ❓ Preguntas Frecuentes

### ¿Cuándo usar Agents vs Chains?
- **Chains**: Cuando el flujo es predecible y lineal
- **Agents**: Cuando necesitas razonamiento y decisiones dinámicas

### ¿Qué tipo de memoria usar?
- **Buffer**: Conversaciones cortas (<10 turnos)
- **Window**: Chatbots generales (mantén últimas 5-10)
- **Summary**: Sesiones largas (>20 turnos)

### ¿Cuántas herramientas puede tener un agente?
- **Recomendado**: 3-7 herramientas
- **Máximo**: 10-15 (performance se degrada)
- **Tip**: Agrupa herramientas similares

### ¿Los agentes son deterministas?
- **No** (debido a la temperatura del LLM)
- Para consistencia: usa temperatura baja (0.1-0.3)
- Para creatividad: usa temperatura alta (0.7-0.9)

---

## 💰 Consideraciones de Costo

### Tokens por componente:

| Componente | Tokens aproximados |
|------------|-------------------|
| Memoria Buffer (10 turnos) | 2000-3000 |
| Memoria Window (k=3) | 500-800 |
| Memoria Summary | 300-500 |
| Agent reasoning (por acción) | 200-400 |
| Tool call | 50-100 |

### Optimizaciones:
1. ✅ Usa Window Memory en vez de Buffer
2. ✅ Limita `max_iterations` del agente
3. ✅ Usa modelos más baratos para razonamiento simple
4. ✅ Cachea resultados de herramientas

---

## 🎓 Evaluación

### El estudiante demuestra dominio cuando puede:
- [ ] Explicar la diferencia entre Chain y Agent
- [ ] Implementar 3 tipos de memoria
- [ ] Crear herramientas personalizadas funcionales
- [ ] Construir un agente que razona correctamente
- [ ] Estructurar salidas con Pydantic
- [ ] Integrar RAG + Agents + Memory en un sistema

---

## 📝 Notas para el Instructor

### Puntos clave a enfatizar:
1. **La descripción de herramientas es CRÍTICA** - El agente decide basándose en ella
2. **ReAct es un patrón, no magia** - Mostrar el razonamiento paso a paso
3. **Memory tiene trade-offs** - No hay solución única
4. **Agents fallan a veces** - Es normal, ajustar prompts y descripciones

### Demos que funcionan bien:
- ✅ Comparación lado a lado de 3 tipos de memoria
- ✅ Ver el razonamiento del agente en verbose=True
- ✅ Mostrar cuándo el agente escoge herramienta incorrecta
- ✅ Live coding de una herramienta personalizada

### Errores comunes de estudiantes:
1. Descripciones de herramientas vagas
2. No limitar `max_iterations`
3. Usar Buffer Memory para todo
4. No validar inputs de herramientas
5. Esperar que el agente sea 100% confiable

---

## 🏆 Proyecto Final Sugerido

**Sistema de Gestión de Proyectos de Construcción**

### Requisitos:
1. **Agente principal** que coordina
2. **3+ herramientas**:
   - Calcular materiales necesarios
   - Asignar equipos según disponibilidad
   - Estimar tiempo y costo
3. **Memoria** que recuerde proyectos anteriores
4. **Output estructurado** con Pydantic
5. **RAG** sobre manuales de equipos

### Bonus:
- Multi-agente (agente de ventas + agente de logística)
- Integración con API real de inventario
- Dashboard de visualización

---

## ✅ Checklist de Preparación

### Antes de la clase:
- [ ] Instalar dependencias: `langchain`, `langchain-openai`, `faiss-cpu`
- [ ] Configurar `.env` con `OPENAI_API_KEY`
- [ ] Tener el PDF del catálogo disponible
- [ ] Probar que todos los ejemplos funcionan
- [ ] Preparar ejemplos de errores comunes

### Materiales necesarios:
- [ ] Jupyter Notebook (`LangChain_Avanzado_Clase2.ipynb`)
- [ ] README con plan de clase
- [ ] PDF del catálogo
- [ ] Archivo `.env` de ejemplo

---

## 📞 Contacto y Soporte

**¿Preguntas después de la clase?**
- Documentación: [LangChain Docs](https://python.langchain.com/)
- Community: [LangChain Discord](https://discord.gg/langchain)
- Stack Overflow: Tag `langchain`

---

**¡Éxitos en la clase! 🚀**
