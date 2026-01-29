# Ejemplo Práctico: Refinamiento por Desplazamiento de Perspectiva

Este documento ilustra cómo utilizar la técnica de **Desplazamiento de Perspectiva** para auditar y fortalecer una idea. Esta técnica consiste en pedirle a la IA que critique o mejore su propio trabajo asumiendo un rol antagónico o complementario.

## Escenario del Caso
**Contexto:** Un equipo de producto ha diseñado una nueva funcionalidad "Gamificada" para una app bancaria. El primer borrador (generado por un rol de Marketing) es muy entusiasta pero podría ignorar riesgos regulatorios o de usuario.

---

## Paso 1: El Prompt Inicial (Generación)

Primero, generamos la idea base usando el marco ROSAS estándar.

```text
**Rol:** Product Manager enfocado en Engagement y Gamificación.
**Objetivo:** Describir los beneficios de la nueva función "Retos de Ahorro" para la app bancaria.
**Situación:** Queremos aumentar la retención de usuarios jóvenes (Gen Z) mediante recompensas inmediatas.
**Acción:** Lista 3 beneficios clave y un slogan atractivo que fomente el uso compulsivo de la app.
```

*(Supongamos que la IA genera una respuesta muy optimista sobre puntos, medallas y diversión adictiva).*

---

## Paso 2: El Prompt de Refinamiento (Desplazamiento de Perspectiva)

Aquí es donde aplicamos la técnica. En lugar de pedir "mejora esto", forzamos un cambio de lente radical para encontrar fallos.

```text
**Instrucción de Refinamiento:**

"Perfecto. Ahora mantén esa propuesta en memoria, pero cambia completamente tu rol.

**Nuevo Rol:** Actúa como un **Chief Risk Officer (CRO)** y Auditor de Cumplimiento Normativo muy conservador.

**Acción:**
1. Critica despiadadamente la propuesta anterior. Busca riesgos de adicción al juego (ludopatía), problemas de privacidad y trivialización de las finanzas.
2. Propón 3 'Guardarraíles' o límites de seguridad que debemos implementar para mitigar estos riesgos sin matar la funcionalidad.
"
```

---

## Paso 3: Síntesis Final (El Resultado Robusto)

```text
"Ahora, actúa como el **CEO**. Integra la creatividad de la propuesta inicial con la seguridad del reporte de riesgos. Redacta la especificación final de la funcionalidad equilibrando ambos mundos."
```

### ¿Por qué funciona esto?
El Desplazamiento de Perspectiva rompe el "sesgo de complacencia" de la IA. Al forzarla a adoptar una postura crítica o antagónica, descubres puntos ciegos que un solo prompt, por muy bueno que sea, no podría revelar.