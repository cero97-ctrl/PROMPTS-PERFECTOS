---
exported: 2026-01-29T01:25:50.609Z
source: NotebookLM
type: report
title: "Guía Práctica: El Poder del Ejemplo (Few-Shot Prompting)"
---

# Guía Práctica: El Poder del Ejemplo (Few-Shot Prompting)

导出时间: 28/1/2026, 9:25:50 p. m.

---

# Guía Práctica: El Poder del Ejemplo (Few-Shot Prompting)

## 1\. La Gran Diferencia: Decir vs. Mostrar

Gigantes tecnológicos como **Google, IBM** y expertos de la talla de **Andrew Ng** coinciden en una realidad incómoda: el 90% de los usuarios interactúa incorrectamente con la Inteligencia Artificial. El error no es técnico, sino comunicativo: intentamos explicar conceptos complejos con instrucciones vagas esperando que la IA "adivine" nuestra intención.

La filosofía para dominar esta herramienta es simple: **mostrar es mejor que decir**. El uso de ejemplos elimina la ambigüedad y sustituye párrafos de descripciones técnicas por modelos claros de ejecución.

"Un ejemplo vale más que 1000 palabras: es más preciso, completo y directo que cualquier descripción."

Para pasar de resultados mediocres a producciones de alta calidad, debemos abandonar la esperanza de que la IA sea vidente y empezar a proporcionarle mapas visuales de lo que esperamos.

\--------------------------------------------------------------------------------

## 2\. Anatomía del Resultado Mediocre (Zero-Shot)

El término **Zero-Shot** se refiere a cuando lanzamos una instrucción sin ninguna referencia previa. En este vacío informativo, la IA se ve obligada a rellenar los huecos mediante suposiciones, lo que deriva en "alucinaciones" o respuestas genéricas y aburridas.

Cuando utilizas una **instrucción genérica**, estás delegando el control creativo a la estadística del modelo, no a tu visión profesional.

```
PROMPT POBRE (Zero-Shot):
"Escribe un post para LinkedIn sobre marketing digital."
```
**Resultado Genérico:** Un texto lleno de clichés, sin una voz propia y que podría haber sido publicado por cualquier marca de cualquier industria. Para tomar el control, implementa la técnica de los expertos: el _Few-shot prompting_.

\--------------------------------------------------------------------------------

## 3\. La Técnica del Few-Shot: Instrucciones con Modelos

El **Few-shot prompting** consiste en incluir de dos a tres ejemplos reales dentro de tu instrucción. Como Learning Designer, te recomiendo usar piezas previas de tu autoría (newsletters, reportes o artículos) para "entrenar" a la IA en tu voz personal sin tener que describirla.

**Regla de Oro:** Los ejemplos no necesitan ser perfectos; solo deben mantener el **formato y la estructura** que deseas que la IA replique.

| Lo que el usuario dice (Instrucción) | Lo que el usuario muestra (Ejemplos) |
| --- | --- |
| "Escribe una newsletter con mi estilo habitual." | "Aquí tienes 2 ejemplos previos: [Ejemplo 1], [Ejemplo 2]." |
| "Redacta un reporte de ventas con este esquema." | "Usa este formato de referencia: [Métrica A: Valor...]" |

\--------------------------------------------------------------------------------

## 4\. Comparación Visual: El Framework ROSAS

Para transformar un prompt mediocre en una herramienta de precisión, utiliza el framework **ROSAS** (Rol, Objetivo, Situación, Acción, Secuencia). Veamos cómo un fotógrafo freelance pasaría de un pedido básico a una propuesta profesional.

**El Prompt "Antes" (Básico):**

```
"Escribe una propuesta para un cliente que quiere fotos para su web."
```
**El Prompt "Después" (Estructurado con ROSAS):**Para elevar el nivel, construye tu instrucción siguiendo este checklist:

• \[ \] **Rol:** "Actúa como un fotógrafo freelance con 10 años de experiencia corporativa."

• \[ \] **Objetivo:** "Redactar una propuesta comercial de alto impacto."

• \[ \] **Situación:** "El cliente es una empresa de tecnología que renueva su imagen web."

• \[ \] **Acción Esperada:** "Generar un texto que destaque el valor técnico y artístico."

• \[ \] **Secuencia/Ejemplo:** "Sigue la estructura de **este ejemplo** de una propuesta exitosa: \[Insertar Ejemplo\]."

**Impacto Real:** Este nivel de detalle permite que una tarea de 30 minutos se resuelva con excelencia en apenas **90 segundos**.

\--------------------------------------------------------------------------------

## 5\. Elevando el Nivel: Ejemplos de Razonamiento (Few-Shot CoT)

Cuando el problema es complejo, no solo muestres el resultado; muestra el **proceso mental**. Esto se conoce como _Few-Shot Chain of Thought_ (Cadena de Pensamiento con ejemplos).

Al darle a la IA casos resueltos paso a paso, el modelo replica tu lógica. Por ejemplo, en un proceso de **decisión de contratación**:

1\. **Analizar el CV:** Evaluar experiencia técnica vs. cultura.

2\. **Identificar Riesgos:** Detectar vacíos en la trayectoria.

3\. **Justificación:** Comparar al candidato con el estándar del equipo.

**Nota de Experto:** Los modelos modernos (como o1 o las últimas versiones de Gemini) ya razonan de forma automática. Sin embargo, el _Few-Shot CoT_ sigue siendo vital para enseñar a la IA **tu método específico** de resolución, asegurando que el "camino" que tome el modelo sea el mismo que tú seguirías.

\--------------------------------------------------------------------------------

## 6\. Iteración y Metaprompting: Los Mandamientos de Google

Si el resultado sigue sin ser óptimo, no abandones la herramienta. Aplica los **4 Mandamientos de Mejora de Google**:

1\. **Contexto y Rol:** Revisa si definiste quién es la IA y para qué sirve la tarea.

2\. **Simplicidad y Estructura:** Divide instrucciones largas en oraciones simples. **Coloca siempre el contexto en la parte superior y las instrucciones finales como una lista al final del prompt.**

3\. **Enfoque Diferente:** Cambia la perspectiva (ej. "Escribe como un experto con 500k seguidores").

4\. **Restricciones:** Establece límites claros (ej. "No uses la palabra 'revolucionario'").

Si no sabes por dónde empezar, utiliza el **Metaprompting** para que la IA diseñe la instrucción por ti:

```
COMANDO DE METAPROMPTING:
"Quiero lograr [Objetivo X]. Hazme todas las preguntas necesarias para entender el contexto y, una vez respondidas, redacta tú mismo el mejor prompt posible para conseguir este resultado."
```
\--------------------------------------------------------------------------------

## 7\. Resumen de la "Fórmula Maestra"

Para dominar la IA siguiendo los estándares de Google, IBM y Andrew Ng, tu flujo de trabajo debe sostenerse en estos 5 pilares:

• **CLARIDAD:** Instrucciones directas y sin rodeos.

• **CONTEXTO:** Antecedentes detallados sobre quién eres y qué necesitas.

• **EJEMPLOS:** Uso de Few-Shot para definir el estilo y formato exacto.

• **RAZONAMIENTO:** Guía lógica para procesos de decisión complejos.

• **ITERACIÓN:** Refinamiento constante basado en resultados.

Has pasado de las instrucciones al azar a un sistema científico. Ahora posees el marco de trabajo de los líderes de la industria; la próxima vez que te enfrentes a un modelo de lenguaje, no escribas lo primero que se te ocurra: **implementa el sistema.**