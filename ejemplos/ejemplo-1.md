# Ejemplo Práctico: Framework ROSAS

Este documento presenta un ejemplo aplicado del marco **ROSAS** (Rol, Objetivo, Situación, Acción, Secuencia) para la generación de un prompt estructurado de alta fidelidad.

## Escenario del Caso
**Contexto:** Un Gerente de Proyecto necesita evaluar los riesgos críticos antes de migrar una base de datos financiera obsoleta a la nube.

## Desglose del Prompt (Estructura ROSAS)

| Componente | Detalle de la Instrucción |
| :--- | :--- |
| **R - Rol** | Senior Technical Project Manager con certificación PMP y especialización en infraestructura Cloud (AWS) y cumplimiento normativo. |
| **O - Objetivo** | Crear una Matriz de Evaluación de Riesgos y un Plan de Contingencia (Rollback) para la migración. |
| **S - Situación** | El cliente es una Fintech sujeta a regulaciones PCI-DSS estrictas. La migración debe ejecutarse en una ventana de 48 horas (fin de semana). La tolerancia a la pérdida de datos es 0%. |
| **A - Acción** | 1. Identificar 5 riesgos técnicos y de cumplimiento. <br> 2. Asignar probabilidad e impacto a cada uno. <br> 3. Definir estrategias de mitigación preventiva y reactiva. |
| **S - Secuencia** | Formato de salida: Tabla Markdown para la matriz y un Resumen Ejecutivo (bullet points) para el CTO. |

---

## Prompt Final (Listo para usar)

```text
**Rol:** Actúa como un Senior Technical Project Manager experto en migraciones a AWS y cumplimiento PCI-DSS.

**Objetivo:** Generar una Matriz de Evaluación de Riesgos detallada y un Plan de Contingencia para la migración de una base de datos legacy.

**Situación:** Trabajamos para una Fintech con tolerancia cero a la pérdida de datos. La migración se realizará en una ventana crítica de 48 horas este fin de semana. El sistema actual es inestable.

**Acción Esperada:**
1. Analiza y lista los 5 riesgos más críticos (técnicos y regulatorios).
2. Evalúa la Probabilidad (Alta/Media/Baja) y el Impacto (Crítico/Alto) de cada uno.
3. Desarrolla una estrategia de mitigación específica y define el "Trigger" exacto que activaría un Rollback.

**Secuencia de Salida:**
1. Presenta la información en una tabla Markdown con las columnas: [Riesgo | Probabilidad/Impacto | Mitigación | Trigger de Rollback].
2. Finaliza con un resumen ejecutivo de 3 puntos clave dirigido al CTO para autorizar el inicio de la operación.
```

---
*Este ejemplo demuestra cómo la especificidad en el Rol y la Situación reduce la entropía y evita respuestas genéricas sobre gestión de riesgos.*