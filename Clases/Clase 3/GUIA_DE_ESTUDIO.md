# 📚 Guía de Estudio - Clase 3: Optimización de Agentes RAG

## 🎯 Objetivo de esta guía
Esta guía te ayudará a prepararte para la Clase 3, asegurando que tengas los conocimientos necesarios para aprovechar al máximo el contenido.

---

## 📋 PARTE 1: Repaso de Fundamentos (Clase 1 y 2)

### 1.1 Conceptos de RAG
- [ ] **¿Qué es RAG?** (Retrieval-Augmented Generation)
  - Entender el flujo: Retrieval → Augmentation → Generation
  - Diferencia entre RAG y LLM sin contexto
  - Ventajas de RAG sobre fine-tuning

- [ ] **Componentes de RAG**
  - Vectorstore (FAISS)
  - Embeddings (text-embedding-3-small)
  - Retriever (búsqueda por similaridad)
  - LLM (gpt-4o-mini)

- [ ] **Proceso de Vectorización**
  - Cómo se crean los embeddings
  - Qué es un chunk y por qué dividimos documentos
  - Búsqueda por similaridad coseno

### 1.2 LangChain Básico
- [ ] **Chains con LCEL**
  - Operador `|` (pipe) para conectar componentes
  - Sintaxis: `prompt | llm | parser`
  - Diferencia entre `.invoke()` y `.stream()`

- [ ] **Prompts**
  - ChatPromptTemplate
  - Variables en prompts: `{variable}`
  - System vs Human messages

- [ ] **Callbacks**
  - Para qué sirven los callbacks
  - `get_openai_callback()` para tracking de costos

### 1.3 OpenAI API
- [ ] **Modelos disponibles**
  - gpt-4o-mini (rápido y económico)
  - gpt-4o (más potente, más caro)
  - Diferencias de precio entre modelos

- [ ] **Tokens**
  - Qué es un token (≈ 0.75 palabras en inglés)
  - Tokens de input vs output
  - Cómo contar tokens en español

- [ ] **Costos**
  - Estructura de precios de OpenAI
  - Input tokens vs Output tokens
  - Cómo calcular costo por consulta

---

## 📋 PARTE 2: Conceptos Nuevos de Clase 3

### 2.1 Prompt Engineering ⭐ IMPORTANTE

#### ¿Qué es?
El arte y ciencia de diseñar instrucciones efectivas para el LLM.

#### Estudiar:
- [ ] **Componentes de un buen prompt**
  - Contexto claro
  - Instrucciones específicas
  - Formato de salida esperado
  - Restricciones y límites

- [ ] **Técnicas de Prompting**

  **Zero-shot:**
  ```
  "Responde la pregunta: ¿Qué es RAG?"
  ```
  ✅ Simple
  ❌ Puede dar respuestas genéricas

  **Few-shot Learning:**
  ```
  "Ejemplos:
   P: ¿Precio del TE-500? R: L320 por día
   P: ¿Precio del TE-70? R: L750 por día

   P: ¿Precio del TE-2000?"
  ```
  ✅ El LLM aprende del formato
  ✅ Respuestas más consistentes

  **Chain of Thought (CoT):**
  ```
  "Piensa paso a paso:
   1. ¿Qué pregunta el usuario?
   2. ¿Qué información tengo?
   3. ¿Cuál es la mejor respuesta?"
  ```
  ✅ Mejora razonamiento
  ✅ Reduce alucinaciones

- [ ] **Role Playing**
  ```
  "Eres un especialista técnico con 25 años de experiencia..."
  ```
  ✅ Da contexto de expertise
  ✅ Mejora el tono de respuestas

- [ ] **Restricciones**
  ```
  "SOLO usa información del contexto"
  "Máximo 3 párrafos"
  "Si no sabes, di 'no tengo información'"
  ```
  ✅ Previene alucinaciones
  ✅ Controla longitud de respuestas

#### 📖 Recursos para estudiar:
- [OpenAI Best Practices](https://platform.openai.com/docs/guides/prompt-engineering)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [Learn Prompting](https://learnprompting.org/)

---

### 2.2 Parámetros del LLM ⭐ IMPORTANTE

#### Temperature (0.0 - 1.0)
Controla la aleatoriedad de las respuestas.

- [ ] **Temperature = 0.0**
  - Determinista (siempre la misma respuesta)
  - Uso: Clasificación, datos estructurados
  - Ejemplo: "Categoriza este producto"

- [ ] **Temperature = 0.3**
  - Consistente pero con variación mínima
  - Uso: **Atención al cliente, FAQ**
  - Ejemplo: Responder preguntas sobre productos

- [ ] **Temperature = 0.7**
  - Creativo y variado
  - Uso: Generación de contenido, marketing
  - Ejemplo: "Escribe un slogan creativo"

- [ ] **Temperature = 1.0**
  - Muy aleatorio
  - Uso: Brainstorming, ideas originales
  - Ejemplo: "Dame 20 ideas de productos nuevos"

#### Max Tokens
Límite máximo de tokens en la respuesta.

- [ ] **¿Cómo elegir?**
  - Respuestas cortas: 100-200 tokens
  - Respuestas normales: 300-500 tokens
  - Respuestas largas: 500-1000 tokens

- [ ] **Impacto en costos**
  - Más tokens = Mayor costo
  - Ajustar al mínimo necesario
  - Monitorear en producción

#### Top P (Nucleus Sampling)
Alternativa a temperature (no se usa en Clase 3, pero es bueno saberlo).

---

### 2.3 Medición de Costos ⭐ IMPORTANTE

#### ¿Por qué medir?
- [ ] Control de presupuesto
- [ ] Optimización de recursos
- [ ] Comparación de configuraciones
- [ ] Proyección de costos a escala

#### Métricas clave:
- [ ] **Tokens de Prompt (Input)**
  - Lo que envías al LLM
  - Incluye: system message + contexto + pregunta
  - Precio: ~$0.15 / 1M tokens (gpt-4o-mini)

- [ ] **Tokens de Completion (Output)**
  - Lo que el LLM genera
  - Solo la respuesta
  - Precio: ~$0.60 / 1M tokens (gpt-4o-mini)

- [ ] **Tokens Totales**
  - Suma de input + output
  - Base para calcular costo

- [ ] **Costo por Consulta**
  - Fórmula:
    ```
    Costo = (tokens_input * precio_input / 1M) +
            (tokens_output * precio_output / 1M)
    ```

#### Usando Callbacks:
```python
from langchain_core.callbacks import get_openai_callback

with get_openai_callback() as cb:
    response = llm.invoke(...)
    print(f"Tokens: {cb.total_tokens}")
    print(f"Costo: ${cb.total_cost}")
```

---

### 2.4 Benchmarking

#### ¿Qué es?
Comparar diferentes configuraciones para encontrar la óptima.

#### Métricas a comparar:
- [ ] **Calidad**
  - Precisión de la respuesta
  - Relevancia
  - Completitud

- [ ] **Costo**
  - $ por consulta
  - Proyección a escala

- [ ] **Velocidad**
  - Tiempo de respuesta
  - Latencia

- [ ] **Tokens**
  - Consumo promedio
  - Variabilidad

#### Proceso:
1. Definir baseline (configuración actual)
2. Crear variantes (diferentes prompts/parámetros)
3. Ejecutar mismas preguntas en todas
4. Comparar métricas
5. Elegir configuración óptima

---

## 📋 PARTE 3: Habilidades Técnicas

### 3.1 Python
- [ ] Diccionarios y listas
- [ ] Funciones con parámetros
- [ ] Format strings: `f"Texto {variable}"`
- [ ] Manejo de excepciones básico
- [ ] Importación de módulos

### 3.2 Jupyter Notebooks
- [ ] Ejecutar celdas (Shift + Enter)
- [ ] Reiniciar kernel
- [ ] Ver outputs
- [ ] Exportar notebooks

### 3.3 Análisis de Datos
- [ ] Calcular promedios
- [ ] Comparar valores
- [ ] Calcular porcentajes de mejora
- [ ] Interpretar tablas comparativas

---

## 📋 PARTE 4: Preparación Práctica

### 4.1 Verificar Ambiente
```bash
# Comprobar instalación de paquetes
pip list | grep langchain
pip list | grep openai
pip list | grep faiss

# Verificar archivos
ls Clases/Clase\ 1/vectorstore_db/
ls .env
```

### 4.2 Repasar Clase 1
- [ ] Ejecutar el notebook de Clase 1
- [ ] Verificar que el vectorstore existe
- [ ] Hacer 2-3 consultas de prueba
- [ ] Revisar cómo funciona el retriever

### 4.3 Repasar Clase 2
- [ ] Entender LCEL (operador `|`)
- [ ] Chains básicas vs secuenciales
- [ ] Tools y function calling
- [ ] Output parsers

---

## 📋 PARTE 5: Ejercicios de Preparación

### Ejercicio 1: Mejorar un Prompt
Dado este prompt básico:
```
"Responde la pregunta sobre equipos"
```

Mejóralo aplicando:
- [ ] Role playing
- [ ] Instrucciones claras
- [ ] Restricciones
- [ ] Formato de salida

**Respuesta sugerida:**
```
"Eres un especialista técnico de Lazarus.
Usa SOLO la información del contexto para responder.
Si no tienes información, di 'No tengo esa información'.
Responde en máximo 3 párrafos, en español formal."
```

### Ejercicio 2: Calcular Tokens Aproximados
Esta pregunta tiene cuántos tokens aproximadamente:
```
"¿Cuál es el mejor equipo para demolición de concreto pesado?"
```

**Pista:** En español, 1 token ≈ 1 palabra
**Respuesta:** ~10 tokens

### Ejercicio 3: Calcular Costos
Si una consulta usa:
- Input: 500 tokens
- Output: 150 tokens
- Modelo: gpt-4o-mini ($0.15/$0.60 por 1M tokens)

¿Cuál es el costo?

**Respuesta:**
```
Input: (500 / 1,000,000) * $0.15 = $0.000075
Output: (150 / 1,000,000) * $0.60 = $0.000090
Total: $0.000165
```

### Ejercicio 4: Elegir Temperature
Para cada caso, elige la temperature adecuada:

- [ ] Chatbot de soporte técnico → **0.3** (consistencia)
- [ ] Generar ideas de marketing → **0.7-0.9** (creatividad)
- [ ] Clasificar productos → **0.0** (determinismo)
- [ ] Escribir descripciones de productos → **0.5** (balance)

---

## 📋 PARTE 6: Glosario de Términos

### Términos Clave

**Prompt Engineering**
: Diseño estratégico de instrucciones para LLMs.

**Temperature**
: Parámetro que controla aleatoriedad (0=determinista, 1=aleatorio).

**Max Tokens**
: Límite máximo de tokens en la respuesta del LLM.

**Token**
: Unidad básica de texto (~0.75 palabras en inglés, ~1 palabra en español).

**Few-shot Learning**
: Dar ejemplos en el prompt para que el LLM aprenda el formato.

**Chain of Thought (CoT)**
: Pedir al LLM que razone paso a paso.

**Callback**
: Función que se ejecuta durante el proceso para tracking/logging.

**Benchmark**
: Comparación sistemática de diferentes configuraciones.

**Baseline**
: Configuración inicial/actual usada como referencia.

**ROI (Return on Investment)**
: Retorno de inversión, beneficio vs costo.

---

## 📋 PARTE 7: Checklist Final de Preparación

### Antes de la Clase 3:

#### Conocimientos
- [ ] Entiendo qué es RAG y cómo funciona
- [ ] Sé qué son los embeddings y vectorstore
- [ ] Conozco la sintaxis básica de LangChain (LCEL)
- [ ] Entiendo qué es un token
- [ ] Sé cómo se calculan los costos en OpenAI

#### Habilidades
- [ ] Puedo ejecutar un notebook de Jupyter
- [ ] Sé usar diccionarios y funciones en Python
- [ ] Puedo interpretar tablas comparativas
- [ ] Entiendo cómo calcular porcentajes y promedios

#### Ambiente
- [ ] Tengo instalados todos los paquetes necesarios
- [ ] Mi API key de OpenAI funciona
- [ ] Existe el directorio `vectorstore_db/` de Clase 1
- [ ] Puedo abrir y ejecutar notebooks

#### Conceptos Nuevos (Estudiar antes)
- [ ] Leí sobre Prompt Engineering (15 min)
- [ ] Entiendo qué es temperature (5 min)
- [ ] Sé cómo se miden tokens y costos (10 min)
- [ ] Comprendo el concepto de benchmarking (5 min)

**Total tiempo de estudio: ~35-45 minutos**

---

## 🎯 Plan de Estudio Sugerido

### Sesión 1 (30 min): Repaso de Fundamentos
1. Re-ejecutar notebook de Clase 1 (15 min)
2. Repasar conceptos de RAG (10 min)
3. Verificar ambiente técnico (5 min)

### Sesión 2 (45 min): Conceptos Nuevos
1. Leer sobre Prompt Engineering (20 min)
   - OpenAI Best Practices
   - Ejemplos de Few-shot y CoT
2. Estudiar parámetros del LLM (15 min)
   - Temperature
   - Max Tokens
3. Entender medición de costos (10 min)
   - Precios de OpenAI
   - Cálculo de tokens

### Sesión 3 (30 min): Práctica
1. Hacer ejercicios de preparación (20 min)
2. Escribir 3 prompts diferentes (10 min)
   - Uno simple
   - Uno con instrucciones
   - Uno con Few-shot

**Total: ~2 horas de preparación**

---

## 📚 Recursos Adicionales

### Documentación Oficial
- [OpenAI Pricing](https://openai.com/pricing)
- [OpenAI API Docs](https://platform.openai.com/docs)
- [LangChain Docs](https://python.langchain.com/docs/get_started/introduction)

### Artículos y Tutoriales
- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [Learn Prompting](https://learnprompting.org/)
- [Chain of Thought Paper](https://arxiv.org/abs/2201.11903)

### Videos (Opcional)
- Buscar en YouTube: "Prompt Engineering Tutorial"
- Buscar: "LangChain Temperature Explained"
- Buscar: "OpenAI Cost Optimization"

---

## ❓ Preguntas Frecuentes

### ¿Cuánto tiempo me tomará la Clase 3?
- Ejecución del notebook: 45-60 min
- Análisis y aprendizaje: 30-45 min
- **Total: ~2 horas**

### ¿Necesito la Clase 2 completada?
No es estrictamente necesaria, pero ayuda entender mejor LCEL y chains.

### ¿Cuánto costará ejecutar los ejercicios?
- Ejercicio 1: ~$0.002 (3 prompts × 1 pregunta)
- Ejercicio 2: ~$0.003 (3 configs × 1 pregunta)
- Ejercicio 3: ~$0.005 (5 preguntas)
- **Total: ~$0.01 (1 centavo de dólar)**

### ¿Qué pasa si no tengo el vectorstore de Clase 1?
Puedes crearlo ejecutando solo las primeras celdas del notebook de Clase 1.

### ¿Puedo usar otro modelo que no sea gpt-4o-mini?
Sí, pero los costos variarán. gpt-4o-mini es el más económico.

---

## ✅ Auto-Evaluación

Antes de comenzar la Clase 3, verifica que puedas responder SÍ a:

1. ¿Entiendo qué es RAG? → [ ]
2. ¿Sé qué es un token? → [ ]
3. ¿Puedo escribir un prompt básico? → [ ]
4. ¿Entiendo qué es temperature? → [ ]
5. ¿Sé cómo se calculan costos en OpenAI? → [ ]
6. ¿Tengo el ambiente técnico listo? → [ ]
7. ¿He repasado los conceptos de Clase 1? → [ ]

**Si respondiste SÍ a 6 o más, estás listo para la Clase 3! 🚀**

---

**¡Mucho éxito en tu aprendizaje! 📚**

*Esta guía fue diseñada para que te prepares efectivamente en ~2 horas.*
