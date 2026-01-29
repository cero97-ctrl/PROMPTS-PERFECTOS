# Ejemplo Práctico: Tree of Thoughts (ToT)

Este documento ilustra cómo aplicar la técnica de **Árbol de Pensamientos** para decisiones estratégicas complejas donde se requiere evaluar múltiples caminos antes de converger en una solución.

## Escenario del Caso
**Contexto:** Una startup de software B2B tiene un presupuesto limitado de $50,000 USD y debe decidir su estrategia de lanzamiento (Go-to-Market) para un nuevo producto de IA.

## Desglose del Prompt (Estructura ToT)

En lugar de pedir "la mejor estrategia", instruimos al modelo para que desarrolle tres enfoques distintos y los compare.

---

## Prompt Final (Listo para usar)

```text
**Rol:** Actúa como un Comité de Estrategia Corporativa compuesto por tres perfiles expertos: un Growth Hacker (agresivo), un CFO (conservador) y un Brand Manager (visionario).

**Objetivo:** Determinar la asignación óptima del presupuesto de $50k para el lanzamiento del producto "AI-Flow".

**Situación:** El mercado está saturado. Necesitamos resultados (Leads cualificados) en menos de 3 meses, pero sin quemar la marca.

**Acción (Tree of Thoughts):**
1. **Rama 1 (Enfoque Performance):** Desarrolla una estrategia centrada 100% en Paid Media (Ads) para retorno inmediato. Analiza riesgos de CAC alto.
2. **Rama 2 (Enfoque Orgánico):** Desarrolla una estrategia centrada en Inbound Marketing y SEO. Analiza riesgos de lentitud.
3. **Rama 3 (Enfoque de Alianzas):** Desarrolla una estrategia centrada en Partners y afiliados. Analiza dependencia de terceros.

**Fase de Evaluación:**
- Critica cada rama buscando fallos lógicos.
- Crea una Matriz de Decisión comparando: Velocidad, ROI estimado y Riesgo.

**Secuencia de Salida:**
1. Detalle de las 3 Ramas.
2. Matriz de Decisión (Tabla Markdown).
3. Recomendación Final (puede ser una de las ramas o una combinación híbrida justificada).
```

---

### ¿Por qué funciona esto?
Al forzar la creación de ramas divergentes, evitas que el LLM se quede con la primera respuesta probabilística (que suele ser la más genérica). Le obligas a explorar el espacio de soluciones antes de converger.