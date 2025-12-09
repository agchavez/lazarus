# 🚀 Clase 3: Optimización de Agentes RAG (Semana 2)

## 📋 Descripción

En esta clase aprenderás a **optimizar** tu agente RAG, llevándolo de un prototipo funcional a un sistema listo para producción. El enfoque está en:

- **Prompt Engineering**: Diseñar prompts efectivos
- **Ajuste de Parámetros**: Optimizar temperature y max_tokens
- **Medición de Costos**: Trackear y reducir costos operativos

## 🎯 Objetivos de Aprendizaje

Al finalizar esta clase, serás capaz de:

1. ✅ Comparar diferentes estrategias de prompts (Minimal, Estándar, Profesional)
2. ✅ Aplicar técnicas de Few-shot Learning y Chain of Thought
3. ✅ Ajustar parámetros del LLM para balancear calidad/costo
4. ✅ Medir tokens y costos en tiempo real con callbacks
5. ✅ Crear benchmarks para comparar mejoras
6. ✅ Tomar decisiones basadas en datos

## 📚 Contenido

### 1. Setup Inicial
- Configuración del ambiente
- Carga del vectorstore de Clase 1 (sin recrear embeddings)

### 2. Prompt Engineering
- **Prompt Minimal**: Instrucciones básicas
- **Prompt Estándar**: Como Clase 1
- **Prompt Profesional**: Few-shot + Chain of Thought

### 3. Medición y Comparación
- Función para trackear: tiempo, tokens, costos
- Comparativa de 3 prompts diferentes
- Análisis de resultados

### 4. Optimización de Parámetros
- Configuración A: Rápido y barato (temp=0.3, tokens=200)
- Configuración B: Balanceado (temp=0.5, tokens=300)
- Configuración C: Creativo (temp=0.7, tokens=400)

### 5. Análisis de Costos
- Costo promedio por consulta
- Proyección para 100 y 1000 consultas
- ROI de las optimizaciones

### 6. Benchmark Final
- Comparación Semana 1 vs Semana 2
- Métricas de mejora
- Recomendaciones

## 🛠️ Requisitos Previos

### Conocimientos
- ✅ Haber completado [Clase 1](../Clase%201/) - RAG básico
- ✅ Entender conceptos de vectorstore y embeddings
- ✅ Familiaridad con LangChain

### Archivos necesarios
- ✅ `vectorstore_db/` - Creado en Clase 1
- ✅ Archivo `.env` con `OPENAI_API_KEY`

### Dependencias
```bash
pip install openai python-dotenv langchain langchain-openai langchain-community pypdf faiss-cpu
```

## 📂 Archivos en esta carpeta

```
Clase 3/
├── README.md                          # Este archivo
├── Semana_2_Optimizacion_RAG.ipynb   # Notebook principal
└── Catalogo_Equipos_Construccion.pdf  # PDF del catálogo
```

## 🚀 Cómo usar este material

### Paso 1: Verificar requisitos
```bash
# Asegúrate de tener el vectorstore de Clase 1
ls ../Clase\ 1/vectorstore_db/
```

### Paso 2: Abrir el notebook
```bash
jupyter notebook Semana_2_Optimizacion_RAG.ipynb
```

### Paso 3: Ejecutar celda por celda
- Lee las explicaciones en cada celda
- Ejecuta el código
- Analiza los resultados
- Experimenta con diferentes configuraciones

## 📊 Conceptos Clave

### 1. Prompt Engineering

**¿Qué es?**
El arte de diseñar instrucciones efectivas para el LLM.

**Técnicas:**
- **Few-shot Learning**: Incluir ejemplos en el prompt
- **Chain of Thought**: Pedir razonamiento paso a paso
- **Role Playing**: Asignar un rol específico al LLM

### 2. Parámetros del LLM

**Temperature (0-1):**
- `0.0`: Determinista, siempre la misma respuesta
- `0.3`: Consistente, ideal para atención al cliente
- `0.7`: Creativo, para generación de contenido
- `1.0`: Muy aleatorio, experimental

**Max Tokens:**
- Límite de longitud de respuesta
- Más tokens = Mayor costo
- Ajustar según necesidad real

### 3. Cost Tracking

**Métricas importantes:**
- **Tokens de prompt**: Lo que envías al LLM
- **Tokens de completion**: Lo que el LLM genera
- **Tokens totales**: Suma de ambos
- **Costo por consulta**: Varía según modelo

**Precios aproximados (gpt-4o-mini):**
- Input: $0.15 / 1M tokens
- Output: $0.60 / 1M tokens

## 🎓 Ejercicios

### Ejercicio 1: Comparar Prompts
Ejecuta la misma pregunta con 3 prompts diferentes y compara:
- Calidad de la respuesta
- Tokens consumidos
- Costo
- Tiempo de respuesta

### Ejercicio 2: Ajustar Parámetros
Prueba diferentes configuraciones de temperature y max_tokens:
- ¿Cuál da mejores respuestas?
- ¿Cuál es más económica?
- ¿Cuál es el mejor balance?

### Ejercicio 3: Calcular ROI
Mide el ahorro logrado con las optimizaciones:
- Costo Semana 1 vs Semana 2
- Ahorro en 1000 consultas
- Mejora en satisfacción del usuario

## 💡 Tips y Mejores Prácticas

### Para Prompts:
1. **Sé específico**: Instrucciones claras = mejores resultados
2. **Usa ejemplos**: Few-shot learning mejora la calidad
3. **Pide paso a paso**: Chain of Thought para razonamientos
4. **Define el rol**: "Eres un experto en..." funciona bien
5. **Limita la respuesta**: "Máximo 3 párrafos" controla longitud

### Para Parámetros:
1. **Empieza con temperature=0.3**: Para aplicaciones de producción
2. **Ajusta max_tokens**: Solo lo necesario, no más
3. **Mide siempre**: Usa callbacks para trackear costos
4. **Prueba iterativamente**: Pequeños cambios, grandes efectos
5. **Documenta**: Guarda las configuraciones que funcionan

### Para Costos:
1. **Usa gpt-4o-mini**: Más barato que gpt-4
2. **Optimiza chunks**: Menos contexto = menos tokens
3. **Cachea cuando puedas**: Evita consultas repetidas
4. **Monitorea en producción**: Costos pueden escalar rápido
5. **Establece límites**: Budget alerts en OpenAI

## 🔍 Resultados Esperados

Después de las optimizaciones, deberías lograr:

- ✅ **20-40% reducción** en tokens consumidos
- ✅ **15-30% reducción** en costos por consulta
- ✅ **10-20% mejora** en tiempo de respuesta
- ✅ **Mejor calidad** en respuestas (más específicas, mejor estructuradas)

## 📈 Comparación: Antes vs Después

### Antes (Semana 1 - Sin optimizar)
```
Costo/consulta: $0.0008
Tokens/consulta: 850
Tiempo: 2.5s
Calidad: 70/100
```

### Después (Semana 2 - Optimizado)
```
Costo/consulta: $0.0005
Tokens/consulta: 600
Tiempo: 1.8s
Calidad: 95/100
```

### Mejora
```
Ahorro de costo: 37.5%
Ahorro de tokens: 29.4%
Reducción de tiempo: 28%
Mejora de calidad: +25 puntos
```

## 🚀 Próximos Pasos

1. **Implementa en producción**: Usa la configuración óptima
2. **Recopila feedback real**: Los usuarios te dirán qué funciona
3. **Itera continuamente**: Las mejoras son un proceso constante
4. **Prepárate para Clase 4**: Técnicas avanzadas de RAG

## 📚 Recursos Adicionales

### Documentación
- [OpenAI Pricing](https://openai.com/pricing)
- [LangChain Callbacks](https://python.langchain.com/docs/modules/callbacks/)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)

### Artículos recomendados
- [Best practices for prompt engineering](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api)
- [Chain of Thought Prompting](https://arxiv.org/abs/2201.11903)
- [Few-shot Learning](https://arxiv.org/abs/2005.14165)

### Comunidad
- [LangChain Discord](https://discord.gg/langchain)
- [OpenAI Community Forum](https://community.openai.com/)

## ⚠️ Solución de Problemas

### Error: "No se encontró vectorstore_db"
**Solución:** Ejecuta primero el notebook de Clase 1 para crear el vectorstore.

### Error: "API key inválida"
**Solución:** Verifica que tu archivo `.env` tenga `OPENAI_API_KEY=sk-...`

### Los costos son muy altos
**Solución:** Reduce max_tokens, usa temperature más bajo, optimiza el prompt.

### Las respuestas son muy cortas
**Solución:** Aumenta max_tokens, ajusta el prompt para pedir más detalle.

### Las respuestas son inconsistentes
**Solución:** Baja la temperature (prueba con 0.3 o menos).

## 🎯 Checklist de Completitud

Marca lo que has logrado:

- [ ] Entiendo qué es prompt engineering
- [ ] Puedo comparar diferentes prompts
- [ ] Sé ajustar temperature y max_tokens
- [ ] Puedo trackear costos con callbacks
- [ ] Entiendo cómo calcular ROI
- [ ] He creado mi propio benchmark
- [ ] Identifiqué la configuración óptima
- [ ] Documenté mis hallazgos
- [ ] Estoy listo para Clase 4

---

**¡Éxito en tu optimización de agentes RAG! 🎓**

*¿Preguntas? Revisa la documentación o consulta con tu instructor.*
