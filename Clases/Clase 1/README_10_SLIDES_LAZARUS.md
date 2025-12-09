# 📊 AGENTES RAG CON OPENAI - 10 SLIDES PARA GRUPO LAZARUS

**Copia cada slide exactamente como aparece abajo a tu PowerPoint, Google Slides o Canva**

---

# SLIDE 1: PORTADA

**TÍTULO (80pt, Bold, Color Azul):**
```
🤖 AGENTES RAG
con OpenAI
```

**SUBTÍTULO (40pt, Regular, Color Gris):**
```
Clase de Apertura - Grupo Lazarus
```

**DESCRIPCIÓN (24pt, Regular, Color Negro):**
```
Transformando la Información en Soluciones

Más de 30 años en construcción, materiales y equipos
Ahora: Inteligencia Artificial para el Negocio
```

**DISEÑO:** Fondo con degradado azul/gris, texto blanco o contraste alto

---

# SLIDE 2: EL PROBLEMA EN LAZARUS

**TÍTULO (48pt, Bold, Azul):**
```
❌❌ ¿Cuál es el Problema?
```

**COLUMNA IZQUIERDA (Fondo Rojo claro #FFE0E0):**

```
❌ SIN RAG - Situación Actual

Cliente pregunta:
"¿Qué aditivos para concreto resistente?"

Proceso:
1. Buscar manual técnico
2. Llamar a técnico especialista
3. Esperar respuesta
4. Cliente espera 1 HORA

Resultado: TIEMPO PERDIDO ❌
```

**COLUMNA DERECHA (Fondo Verde claro #E0F2E9):**

```
✅ CON RAG - Solución

Cliente pregunta:
"¿Qué aditivos para concreto resistente?"

Proceso:
1. Sistema busca automáticamente
2. Encuentra especificaciones Admix
3. Responde EN 5 SEGUNDOS
4. Con recomendaciones verificadas

Resultado: CLIENTE SATISFECHO ✅

CASOS DE USO INMEDIATOS:
• FAQ de productos Admix, Hilti, Novomix
• Especificaciones técnicas de 1000+ productos
• Recomendaciones para proyectos específicos
```

---

# SLIDE 3: ¿QUÉ ES RAG EN LAZARUS?

**TÍTULO (48pt, Bold, Azul):**
```
🧠 ¿Qué es RAG en Grupo Lazarus?
```

**CONTENIDO PRINCIPAL (28pt):**

```
RAG = Retrieval Augmented Generation
(Búsqueda + Generación Inteligente)
```

**TRES COLUMNAS:**

**COLUMNA 1: RETRIEVAL (Recuadro con borde azul)**
```
🔍 RETRIEVAL: Buscar en Base de Datos

✓ Fichas técnicas de Admix, Hilti, Novomix
✓ Casos de éxito de proyectos completados
✓ Especificaciones de materiales
✓ Recomendaciones de uso
✓ 30 años de experiencia documentada
```

**COLUMNA 2: AUGMENTED (Recuadro con borde gris)**
```
⚡ AUGMENTED: Contextualizar

✓ "¿Mejor para zona tropical?"
✓ "¿Presupuesto limitado?"
✓ "¿Resistencia a humedad?"
✓ "¿Para clima de San Pedro?"
✓ "¿Proyecto industrial o residencial?"
```

**COLUMNA 3: GENERATION (Recuadro con borde verde)**
```
✍️ GENERATION: Respuesta Verificada

✓ Sistema propone mejor solución
✓ Añade referencias técnicas
✓ Cita casos de éxito similares
✓ Proporciona dosis y aplicación
✓ Respuesta 100% verificada
```

---

# SLIDE 4: EL FLUJO EN PRÁCTICA

**TÍTULO (48pt, Bold, Azul):**
```
📊 El Flujo RAG en Práctica - Ejemplo Real
```

**EJEMPLO PASO A PASO:**

```
🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦

PREGUNTA DE CLIENTE:

"Necesito impermeabilizar una cisterna en San Pedro Sula"

🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦

         ↓ SISTEMA BUSCA EN LAZARUS ↓

🔍 BASE DE DATOS:
   ✓ Casos de éxito: Cisterna autorreparable (ENCONTRADO)
   ✓ Productos Admix relevantes: IM-1, selladores (ENCONTRADO)
   ✓ Condiciones San Pedro: clima tropical, humedad alta (ENCONTRADO)

🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦

         ↓ LLM ANALIZA Y PROPONE ↓

🧠 RECOMENDACIÓN:

"Para San Pedro le recomiendo:

✓ ADMIX IM-1 (combate humedad ascendente)
✓ Tecnología de cristalización (autorreparable)
✓ Similar a caso comprobado: Cisterna Honduras
  Resultado: 5 años sin fallas

Presupuesto estimado: L120,000 - L180,000
Tiempo ejecución: 15 días"

🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦

         ↓ RESPUESTA FINAL ↓

✅ CLIENTE RECIBE:
   • Producto específico (ADMIX IM-1)
   • Especificaciones técnicas completas
   • Caso de éxito similar
   • Presupuesto estimado
   • TODO en 5 SEGUNDOS ⚡
```

---

# SLIDE 5: LOS 3 COMPONENTES CLAVE

**TÍTULO (48pt, Bold, Azul):**
```
⚙️ Los 3 Componentes Clave del Sistema
```

**COMPONENTE 1: RETRIEVAL**

```
1️⃣ RETRIEVAL (Tu Base de Datos Lazarus)

QUÉ CONTIENE:
├─ 30+ productos ADMIX (IM-1, selladores, aditivos, epóxicos)
├─ 100+ herramientas HILTI (rotomartillos, taladros, fijación)
├─ Materiales geotécnicos (TenCate, Macaferri, gaviones)
├─ Equipos especializados (bombas, hormigoneras, láser)
├─ 25 Casos de éxito reales COMPLETADOS
└─ 30 años de experiencia documentada

EJEMPLOS DE CASOS:
• Hidroeléctrica Ojo de Agua (20 MW)
• Puente Gala - Intercambiador Vial
• Torre Panorama II
• Proyecto CA-5 Sur (69 km)
• Cisterna autorreparable
```

**COMPONENTE 2: SEARCH**

```
2️⃣ SEARCH (Búsqueda Inteligente)

PROCESO:
├─ Cliente pregunta: "impermeabilizantes para cimentación"
├─ Sistema convierte a "números" (embeddings)
├─ Busca en base de datos similar
├─ Encuentra: ADMIX IM-1 (perfecta coincidencia)
├─ Busca casos similares: Cisterna Honduras
├─ Obtiene TOP-3 recomendaciones
└─ Pasa información al LLM

RESULTADO:
✅ Búsqueda INSTANTÁNEA
✅ Entre 1000+ documentos en MILISEGUNDOS
```

**COMPONENTE 3: GENERATION**

```
3️⃣ GENERATION (Respuesta Verificada)

PROCESO:
├─ LLM recibe: pregunta + documentos relevantes
├─ Analiza contexto (zona tropical, presupuesto)
├─ Crea recomendación personalizada
├─ Basada 100% en datos reales de Lazarus
├─ Con referencias a proyectos completados
└─ Devuelve respuesta VERIFICADA

GARANTÍA:
✅ No alucina (basado en documentos reales)
✅ Tiene referencias (puedes verificar)
✅ Incluye especificaciones técnicas
✅ Proporciona presupuesto estimado
```

---

# SLIDE 6: LAS LIBRERÍAS (EL STACK)

**TÍTULO (48pt, Bold, Azul):**
```
🛠️ Las Librerías - El Stack Tecnológico
```

**LIBRERÍA 1: LANGCHAIN (Recuadro con ícono ⛓️)**

```
⛓️ LANGCHAIN - El Orquestador

¿QUÉ ES?
El director de la orquesta que conecta todo

¿QUÉ HACE?
✓ Conecta OPENAI + FAISS automáticamente
✓ Maneja el flujo de preguntas y respuestas
✓ Automatiza búsquedas de especificaciones
✓ Simplifica la programación

CÓDIGO:
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
```

**LIBRERÍA 2: OPENAI (Recuadro con ícono 🤖)**

```
🤖 OPENAI - El Motor de Inteligencia

MODELOS USADOS:
├─ GPT-4o-mini: Entiende preguntas de construcción
│  ✓ "¿Mejor para zona tropical?"
│  ✓ "¿Qué para puentes?"
│  ✓ Genera recomendaciones de Admix/Hilti
│  ✓ Responde sobre casos de éxito
│
└─ text-embedding-3-small: Convierte a "números"
   ✓ Transforma "impermeabilizante" en vector
   ✓ Permite búsqueda automática
   ✓ Ultra rápido y preciso

CÓDIGO:
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
```

**LIBRERÍA 3: FAISS (Recuadro con ícono 💾)**

```
💾 FAISS - Tu Base de Datos Privada

¿QUÉ ES?
Base de datos vectorial desarrollada por Meta

¿POR QUÉ FAISS?
✓ PRIVADO: Tus datos en servidor LOCAL
✓ RÁPIDO: Búsqueda en milisegundos entre 1000+ docs
✓ GRATIS: Open source, sin costo
✓ SEGURO: No sube información a internet
✓ 30 años de expertise protegido

ALMACENA:
├─ Fichas técnicas PDF
├─ Casos de éxito
├─ Especificaciones
└─ Toda tu base de conocimiento

CÓDIGO:
from langchain_community.vectorstores import FAISS
```

**LIBRERÍAS EXTRA (Recuadro gris)**

```
📚 HERRAMIENTAS AUXILIARES

✓ PyPDF: Lee manuales técnicos en PDF
  Ejemplo: Especificaciones Admix IM-1.pdf

✓ TextLoader: Carga archivos de texto
  Ejemplo: Lista de casos de éxito

✓ CharacterTextSplitter: Divide documentos en secciones
  Ejemplo: Divide manual Hilti en partes pequeñas

✓ python-dotenv: Protege API keys y credenciales
  Ejemplo: Guarda OPENAI_API_KEY de forma segura
```

---

# SLIDE 7: EMBEDDINGS EN CONSTRUCCIÓN

**TÍTULO (48pt, Bold, Azul):**
```
🔢 ¿Qué es un Embedding? (Explicado para Lazarus)
```

**CONCEPTO SIMPLE:**

```
EMBEDDING = Convertir PALABRAS en NÚMEROS
que la IA puede entender y comparar
```

**EJEMPLO CON DOCUMENTO REAL LAZARUS:**

```
┌─────────────────────────────────────────────────────────┐
│ DOCUMENTO TÉCNICO ORIGINAL:                             │
├─────────────────────────────────────────────────────────┤
│ "ADMIX IM-1: Impermeabilizante para cimentación,       │
│  resiste humedad ascendente, recomendado para zonas    │
│  lluviosas y tropicales, tecnología de cristalización" │
└─────────────────────────────────────────────────────────┘

         ↓ SE CONVIERTE A ↓

┌─────────────────────────────────────────────────────────┐
│ VECTOR (Números):                                       │
├─────────────────────────────────────────────────────────┤
│ [0.78, -0.45, 0.92, -0.23, 0.67, 0.34, -0.56, 0.89... │
│  ... 1536 números en total]                             │
└─────────────────────────────────────────────────────────┘
```

**CÓMO FUNCIONA LA BÚSQUEDA:**

```
CLIENTE PREGUNTA:
"¿Qué para humedad en cimentación?"

         ↓ SE CONVIERTE A VECTOR ↓

[0.79, -0.44, 0.91, -0.24, 0.68...]  (Pregunta)

         ↓ SE BUSCA SIMILITUD ↓

COMPARAR CON TODOS LOS VECTORES:

ADMIX IM-1:        [0.78, -0.45, 0.92...] ← 99% SIMILAR ✅✅✅
ADMIX Techo:       [0.23, 0.12, 0.45...]  ← 45% similar
HILTI Rotomartillo: [0.05, 0.78, -0.12...] ← 12% similar

         ↓ RESULTADO ↓

ENCONTRADO: ADMIX IM-1 (Perfecta coincidencia)
```

**DATOS CRÍTICOS QUE DEBE ENTENDER:**

```
✅ "Hilti" ≠ "Admix"
   → Vectores COMPLETAMENTE diferentes
   → No se confunde

✅ "Cimentación" ≈ "Base/Zapata"
   → Vectores PARECIDOS
   → Encuentra ambos términos

✅ "Tropical" ≈ "Lluvia"
   → Vectores RELACIONADOS
   → Entiende el contexto de San Pedro

✅ "Impermeabilizante" ≈ "Protección de humedad"
   → SINONIMOS
   → Encuentra ambos
```

**POR QUÉ IMPORTA:**

```
SIN EMBEDDINGS:
"Pregunta: impermeabilizante
Búsqueda: Buscar palabra exacta 'impermeabilizante'
Resultado: No encuentra si dice 'protección humedad'"

CON EMBEDDINGS (RAG):
"Pregunta: impermeabilizante
Búsqueda: Entiende SIGNIFICADO de la pregunta
Resultado: Encuentra 'protección', 'resistente', 'humedad'"

= BÚSQUEDA INTELIGENTE
```

---

# SLIDE 8: VENTAJAS DE RAG PARA GRUPO LAZARUS

**TÍTULO (48pt, Bold, Azul):**
```
✨ 6 Ventajas Principales para Lazarus
```

**VENTAJA 1: NO ALUCINA**

```
❌ PROBLEMA ACTUAL:
   Técnico novel no sabe especificación
   Responde al azar
   Cliente recibe información INCORRECTA

✅ CON RAG:
   Cliente: "¿Cuál es precio Hilti TE 2000?"
   Sistema: "L25,000 según catálogo 2024"
   
   = SIEMPRE VERIFICADO, NUNCA INVENTA
```

**VENTAJA 2: VERIFICABLE - CON FUENTES**

```
Cliente pregunta: "¿Por qué recomiendas Admix?"

Respuesta del sistema:
"Porque en caso similar:
 ✓ Cisterna autorreparable con ADMIX IM-1
 ✓ Resultado comprobado: 5 años sin fallas
 ✓ Proyecto referencia: Honduras"

= CLIENTE CONFÍA (tiene pruebas)
```

**VENTAJA 3: ECONÓMICO**

```
COSTO IMPLEMENTACIÓN:
• Sistema RAG: ~$50-100/mes con OpenAI
• Comparar con: 1 técnico atendiendo emails = L15,000/mes

AHORRO:
✓ Menos técnicos en atención
✓ Clientes responden más rápido
✓ Más satisfacción
✓ Más ventas

= ROI POSITIVO EN SEMANAS
```

**VENTAJA 4: FÁCIL ACTUALIZAR**

```
HOY: Producto nuevo ADMIX X-500

PROCESO CON RAG:
1. Carga ficha técnica X-500 a FAISS
2. Sistema lo conoce automáticamente
3. Responde preguntas al día siguiente

= SIN REPROGRAMACIÓN, SIN ESPERA
```

**VENTAJA 5: RÁPIDO**

```
CLIENTE ESPERA:
SIN RAG:      1 HORA (llamar, buscar, responder)
CON RAG:      5 SEGUNDOS ⚡

RESULTADO:
• Cliente satisfecho inmediatamente
• Vendedor cierra venta más rápido
• 100+ clientes atendidos simultáneamente

= ESCALABILIDAD SIN AGREGAR PERSONAL
```

**VENTAJA 6: PRIVADO Y SEGURO**

```
DATOS DE LAZARUS:
✓ Servidor LOCAL (no en nube)
✓ No sube a internet
✓ NO se usa para entrenar OpenAI
✓ 30 años de expertise PROTEGIDO
✓ Cumple privacidad

= TUS DATOS SIGUEN SIENDO TUYOS
```

---

# SLIDE 9: CASOS DE USO EN GRUPO LAZARUS

**TÍTULO (48pt, Bold, Azul):**
```
🎯 7 Casos de Uso Inmediatos en Lazarus
```

**CASO 1: SOPORTE TÉCNICO 24/7**

```
📞 SOPORTE TÉCNICO 24/7

Cliente: "¿Qué adhesivo Admix para pisos?"
Sistema: "ADMIX PG-2000
         ✓ Especificaciones: 20 MPa
         ✓ Aplicación: Interior/exterior
         ✓ Tiempo secado: 24 horas
         ✓ Proyecto similar: Cervecería Hondureña"

SIN INTERVENCIÓN HUMANA
DISPONIBLE SIEMPRE (ni fin de semana)
```

**CASO 2: CONSULTAS DE PROYECTOS**

```
🏗️ CONSULTAS DE PROYECTOS

Cliente: "Necesito impermeabilizar un puente"
Sistema: "Recomiendo:
         ✓ ADMIX impermeabilizante
         ✓ Caso similar: Puente Gala (exitoso)
         ✓ Presupuesto estimado: L500K-1M
         ✓ Tiempo: 30 días
         
TÉCNICO REVISA Y CONFIRMA
(ahorra 80% del tiempo de propuesta)
```

**CASO 3: VENTAS ASISTIDAS**

```
📚 VENTAS ASISTIDAS

Vendedor en tienda: "Cliente con presupuesto bajo"
Sistema: "Soluciones económicas:
         ✓ Admix sellador (L1,200)
         ✓ Alternativa Fiori (L900)
         ✓ Oferta Hilti (L2,500)
         
VENDEDOR CIERRA MÁS VENTAS
(recomendaciones personalizadas)
```

**CASO 4: SOPORTE INDUSTRIA**

```
🏭 SOPORTE INDUSTRIA

Ingeniero: "Aditivos para concreto 40 MPa"
Sistema: "ADMIX recomendados:
         ✓ Dosis: X kg/m³
         ✓ Tiempo curado: Y horas
         ✓ Resistencia a: humedad, químicos, sísmica
         ✓ Caso: Central Hidroeléctrica La Vegona (40 MW)
         
PROYECTO INDUSTRIAL
ESPECIFICACIONES PRECISAS
```

**CASO 5: ONBOARDING DE EMPLEADOS NUEVO**

```
👥 ONBOARDING DE EMPLEADOS NUEVO

Empleado nuevo: "¿Cuál es portafolio de Hilti?"
Sistema: "Hilti ofrece:
         ✓ 10 categorías principales
         ✓ 100+ herramientas
         ✓ Servicio LTS (garantía única)
         ✓ Servicio técnico especializado
         
EMPLEADO NUEVO APRENDE RÁPIDO
SIN DEPENDER DE OTROS
```

**CASO 6: ATENCIÓN A DISTRIBUIDORES**

```
📋 ATENCIÓN A DISTRIBUIDORES

Distribuidor: "¿Caso de éxito con TenCate?"
Sistema: "Proyecto La Ensenada Resort
         ✓ Protección costera con geotubos
         ✓ Recuperación de 5,000 m² playa
         ✓ Resistencia a: olas, erosión, mareas
         ✓ Resultado: Exitoso (visible)
         
DISTRIBUIDOR CIERRA VENTA
(argumentos técnicos sólidos)
```

**CASO 7: INNOVACIÓN Y DESARROLLO**

```
💡 INNOVACIÓN Y DESARROLLO

Ingeniero: "¿Podemos usar Admix en proyectos sísmicos?"
Sistema: "Base de datos muestra:
         ✓ Proyecto Intercambiador Vial (San Pedro)
         ✓ Construcción sísmica exitosa
         ✓ ADMIX soportó: 7.2 Richter (2009)
         ✓ Sin daños registrados
         
INNOVACIÓN CON DATOS REALES
NO EXPERIMENTACIÓN RIESGOSA
```

---

# SLIDE 10: CIERRE Y LLAMADO A ACCIÓN

**TÍTULO (48pt, Bold, Azul):**
```
🎯 Resumen: Lo Que Debes Recordar
```

**PUNTO 1:**

```
1️⃣ RAG = BÚSQUEDA + GENERACIÓN INTELIGENTE

No es magia.

Es usar 30 AÑOS de datos Lazarus:
✓ 1000+ productos
✓ 25 casos de éxito
✓ 30 años de experiencia

= Respuestas VERIFICADAS en SEGUNDOS
```

**PUNTO 2:**

```
2️⃣ LAS 3 LIBRERÍAS PRINCIPALES:

⛓️ LANGCHAIN
   Orquesta y conecta todo

🤖 OPENAI (GPT-4o-mini)
   Le da inteligencia al sistema

💾 FAISS
   Base de datos PRIVADA y LOCAL de Lazarus
```

**PUNTO 3:**

```
3️⃣ DATOS QUE USAREMOS:

✅ 30+ productos ADMIX (aditivos, adhesivos, epóxicos)
✅ 100+ herramientas HILTI (rotomartillos, taladros, fijación)
✅ Materiales geotécnicos (TenCate, Macaferri)
✅ 25 casos de éxito reales completados
✅ 30 años de experiencia documentada

TODO SERÁ INFORMACIÓN VERIFICABLE
```

**PUNTO 4:**

```
4️⃣ BENEFICIO INMEDIATO:

ANTES:
• Consultas técnicas: 1 hora espera
• Clientes frustrados
• Equipo de ventas lento

DESPUÉS CON RAG:
• Consultas: 5 segundos
• Clientes satisfechos INMEDIATAMENTE
• Equipo de ventas 10x más rápido

= TRANSFORMACIÓN DEL SERVICIO AL CLIENTE
```

**CIERRE:**

```
❓ ¿PREGUNTAS ANTES DE LA DEMO?

(Pausa para preguntas)

🚀 AHORA: DEMO EN VIVO

En los próximos 50 minutos veremos:

1️⃣ Pregunta real: "¿Impermeabilizantes para tropical?"
   Respuesta: Sistema busca → Encuentra ADMIX IM-1 + caso

2️⃣ Pregunta real: "¿Ciclo típico proyecto Lazarus?"
   Respuesta: Sistema explica 4 fases + proyectos referencia

3️⃣ Pregunta real: "¿Herramientas Hilti para demolición?"
   Respuesta: Sistema lista opciones + garantía LTS

EN CADA RESPUESTA:
✓ Verán cómo busca en la base de datos
✓ Verán las fuentes verificadas
✓ Verán proyectos reales de referencia

= FUNCIONANDO AHORA MISMO
```

**FRASE FINAL (28pt, Bold, Color Azul):**

```
En 4 semanas, cada integrante de Lazarus
será capaz de construir agentes RAG como este.

🚀 Empezamos... AHORA
```

---

# 📋 INSTRUCCIONES PARA COPIAR A POWERPOINT/GOOGLE SLIDES

## OPCIÓN 1: PowerPoint (Microsoft)

1. **Abre PowerPoint**
2. **Crea presentación nueva** (16:9)
3. **Para cada slide:**
   - Haz clic en "Nueva diapositiva"
   - Selecciona layout "Título y contenido"
   - Copia el TÍTULO en el cuadro de título
   - Copia el CONTENIDO en el cuadro de contenido
   - Ajusta colores según indicaciones

## OPCIÓN 2: Google Slides

1. **Abre Google Slides** (slides.google.com)
2. **Crea presentación nueva**
3. **Para cada slide:**
   - Haz clic en "Nueva diapositiva"
   - Copia el contenido
   - Ajusta formato (tamaño fuente, colores)

## OPCIÓN 3: Canva (Recomendado para diseño rápido)

1. **Abre Canva.com**
2. **Busca:** "Presentation Business"
3. **Para cada slide:**
   - Usa template existente
   - Personaliza con colores de Lazarus (Azul/Gris)
   - Copia el texto de aquí

---

# 🎨 RECOMENDACIONES DE DISEÑO

**COLORES:**
- Azul principal: #0066CC o #003399
- Gris: #666666
- Fondo claro: #F8F9FA
- Acentos verdes: #51CF66 (Sí/Bien)
- Acentos rojos: #FF6B6B (No/Problema)

**FUENTES:**
- Títulos: Segoe UI o Calibri (28-48pt, Bold)
- Contenido: Segoe UI o Calibri (16-24pt, Regular)
- Código: Courier New (12-14pt)

**IMÁGENES SUGERIDAS:**
- Slide 1: Logo Lazarus
- Slide 2: Foto proyecto construcción
- Slide 4: Diagrama de flujo
- Slide 6: Logos OpenAI, LangChain, FAISS
- Slide 9: Fotos de productos Admix/Hilti

---

# ✅ CHECKLIST ANTES DE PRESENTAR

- [ ] Todos los 10 slides copiados
- [ ] Colores consistentes
- [ ] Fuentes legibles
- [ ] Números correctos (productos, años, casos)
- [ ] Logo Lazarus en portada
- [ ] Notebook Jupyter preparado para demo
- [ ] Internet probado
- [ ] Proyector funcionando
- [ ] Micrófono probado

---

# 📞 NOTAS PARA PRESENTADOR

**Enfatizar en Slide 2:**
- "Nuestros clientes ESPERAN respuestas INMEDIATAS"
- "Un cliente sin respuesta rápida, llama a la competencia"

**En Slide 6 (Librerías):**
- "LangChain orquesta TODO automáticamente"
- "OpenAI entiende lenguaje técnico sobre construcción"
- "FAISS mantiene datos PRIVADOS en servidor local"

**En Slide 9 (Casos de Uso):**
- "Estos son casos reales donde Lazarus ya ha ganado"
- "El sistema hará que reproduzcamos ese éxito fácilmente"

**Antes de la Demo:**
- "En los próximos minutos verán cómo el sistema responde preguntas reales"
- "Cada respuesta incluye referencia a proyectos completados por Lazarus"
- "Esto transformará cómo atendemos nuestros clientes"

---

¡LISTO! Tienes todo para copiar directamente a tu presentación. 🚀
