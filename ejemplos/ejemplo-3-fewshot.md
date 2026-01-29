# Ejemplo Práctico: Few-Shot Prompting (Estilo y Tono)

Este documento demuestra el uso de la técnica **Few-Shot Prompting** para calibrar con alta precisión el estilo, tono y formato de la IA, basándose en el principio "mostrar es mejor que decir".

## Escenario del Caso
**Contexto:** Una analista financiera debe redactar un resumen semanal del mercado para el comité ejecutivo (CEO, CFO). El estilo debe ser extremadamente conciso, directo y basado en datos, eliminando cualquier lenguaje vago o corporativo.

## Desglose del Prompt (Estructura Few-Shot)

En lugar de describir el tono ("sé profesional y directo"), le proporcionamos a la IA ejemplos concretos del resultado esperado y, crucialmente, de lo que debe evitar.

---

## Prompt Final (Listo para usar)

```text
**Rol:** Actúa como una Analista Financiera Senior del equipo de Estrategia de Inversión, reportando directamente al CFO.

**Objetivo:** Redactar un resumen ejecutivo sobre el estado actual del mercado de vehículos eléctricos (EVs) para el comité de dirección.

**Situación:** La audiencia tiene un conocimiento financiero profundo pero tiempo limitado. Valoran la densidad de datos sobre la prosa. El resumen no debe exceder las 150 palabras.

**Acción:** Analiza los siguientes datos brutos y sintetízalos en un párrafo ejecutivo:
- Ventas globales de EVs Q3: +23% YoY.
- Tesla (TSLA): Market share cae del 65% al 58% a pesar de un aumento de ventas del 15%.
- BYD: Market share aumenta al 17%.
- Margen bruto promedio del sector: 18% (vs 22% el año pasado) debido a la guerra de precios.
- Riesgo regulatorio: Posibles aranceles del 25% en la UE a importaciones chinas.

**Secuencia y Estilo (Few-Shot Prompting):**
Usa el siguiente estilo y formato.

**EJEMPLO POSITIVO (A SEGUIR):**
"Q3 2023: El sector de semiconductores creció un 5.2% QoQ, impulsado por la demanda de IA en centros de datos. NVDA lidera con un +15% en ingresos, mientras que INTC enfrenta una contracción del -3% por retrasos en su nodo de 7nm. El riesgo principal para Q4 es la restricción de exportaciones a China."

**EJEMPLO NEGATIVO (A EVITAR):**
"En el último trimestre, el mundo de los semiconductores ha experimentado un viaje fascinante, con algunos jugadores alcanzando nuevas alturas. La inteligencia artificial sigue siendo un motor revolucionario que está cambiando el paradigma del sector."

Genera el resumen del mercado de EVs siguiendo estrictamente el formato del **EJEMPLO POSITIVO**.
```

---

### ¿Por qué funciona esto?
Al proporcionar un **ejemplo positivo** y uno **negativo**, creamos un contraste claro que permite al modelo entender no solo qué hacer, sino también qué no hacer. Esto es mucho más eficaz que usar adjetivos subjetivos como "profesional" o "conciso", ya que el modelo aprende directamente del patrón estructural y léxico.