# Implementación de un programa básico en Python

En un contexto de aprendizaje de programación, se ha identificado una brecha en la comprensión de los conceptos básicos de Python. El objetivo es que el participante desarrolle un programa simple que involucre la manipulación de datos y la toma de decisiones. El programa debe leer un archivo de texto, filtrar líneas que contengan una palabra específica y escribir las líneas filtradas en un nuevo archivo. El participante deberá enfrentar decisiones sobre cómo estructurar el código y manejar posibles errores de lectura/escritura.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | Python |
| **Nivel** | trainee-l2 |
| **Tipo** | practical |
| **Tiempo estimado** | 2 horas |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y generará un ZIP listo para usar.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Python 3.10+, pip, VS Code o similar.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y generará un archivo ZIP descargable. Descárgalo y extráelo en la carpeta donde quieras trabajar.
- Ejecuta `pip install -r requirements.txt` y luego arranca el proyecto. Si no hay errores, estás listo.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no genera el ZIP automáticamente al terminar el análisis, escríbele: "genera el ZIP ahora".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Lectura y escritura de archivos

**Objetivo:** Implementar la lectura de un archivo de texto y escribir las líneas filtradas en un nuevo archivo.

**Tiempo estimado:** 1 hora

**Instrucciones:**

- Identificar y abrir un archivo de texto existente.
- Leer cada línea del archivo.
- Filtrar líneas que contengan la palabra 'Python'.
- Escribir las líneas filtradas en un nuevo archivo.
- Manejar posibles errores de lectura/escritura.

**Entregable:** Programa que lee un archivo de texto, filtra líneas con la palabra 'Python' y escribe en un nuevo archivo.

<details>
<summary>Pistas de conocimiento</summary>

- Considera cómo manejar errores de lectura/escritura.
- Piensa en la estructura del código para que sea legible y mantenible.

</details>

### Fase 2: Mejora y refactorización

**Objetivo:** Mejorar el programa para que sea más eficiente y manejar más casos de error.

**Tiempo estimado:** 1 hora

**Instrucciones:**

- Refactorizar el código para mejorar la eficiencia.
- Añadir manejo de más casos de error, como archivo no encontrado o permisos insuficientes.
- Asegurar que el programa sea robusto y mantenible.

**Entregable:** Programa refactorizado que maneja más casos de error y es más eficiente.

<details>
<summary>Pistas de conocimiento</summary>

- Considera usar estructuras de datos más eficientes.
- Piensa en cómo mejorar la legibilidad y mantenibilidad del código.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué es un archivo de texto y cómo se lee/escribe en Python?
- **paraQueSirve**: ¿Para qué sirve filtrar líneas en un archivo de texto?
- **comoSeUsa**: ¿Cómo se usa Python para manipular archivos de texto?
- **erroresComunes**: ¿Cuáles son los errores comunes al leer/escribir archivos en Python y cómo se manejan?
- **queDecisionesImplica**: ¿Qué decisiones implica la estructuración del código para este programa?

## Criterios de Evaluacion

- Implementación correcta de la lectura y escritura de archivos.
- Filtrado correcto de líneas con la palabra 'Python'.
- Manejo adecuado de errores de lectura/escritura.
- Refactorización del código para mejorar la eficiencia y mantenibilidad.

## Como trabajar con un asistente de IA

Hay dos caminos, elegi uno:

- **AGENTS.md** (recomendado) — instrucciones nativas del repo. Abri esta carpeta con tu agente local (Claude Code, Cursor, Codex, Copilot, Gemini) y las carga solo. Sabe que archivos faltan y con que comando se verifica, y completa el scaffold escribiendo en disco.
- **PROMPT_MEJORA.md** — para copiar y pegar en un chat (claude.ai, ChatGPT). Devuelve un ZIP con el proyecto. Sirve si no tenes un agente en el IDE.

Ninguno de los dos resuelve las fases del reto: eso es tu trabajo.

## Verificacion

El proyecto esta listo para trabajar cuando este comando corre sin errores:

```bash
pip install -r requirements.txt && python -c "import app.main"
```

---

*Reto generado automaticamente por Challenge Generator - Pragma*
