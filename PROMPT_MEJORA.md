# Prompt para Mejorar el Codigo Base

Copia y pega el contenido del bloque de abajo en un asistente de IA (Claude, ChatGPT)
para obtener un ZIP con el proyecto completo y arrancable.

Si preferis trabajar en tu editor con un agente local (Claude Code, Cursor, Copilot), usa `AGENTS.md` en vez de este archivo: dice lo mismo pero para que escriba los archivos en disco.

## Las dos reglas que no se negocian

1. **Completa el boilerplate.** Todo lo que el proyecto necesita para compilar y arrancar: manifiesto de dependencias, punto de entrada, configuracion, capa de interfaz, y las capas del patron arquitectonico declarado. Eso es andamiaje y es tu trabajo.
2. **NO resuelvas el reto.** Los entregables de las fases son el trabajo de la persona. El hueco pedagogico se deja como esta: el proyecto arranca, pero lo que el reto pide implementar NO esta implementado.

Dicho de otra forma: si algo impide compilar, arreglalo. Si algo es logica de negocio incompleta, validaciones ausentes, un secreto hardcodeado o un patron mejorable, dejalo exactamente como esta — es lo que la persona tiene que encontrar.

## Superficie de practica — NO resuelvas

Estos archivos SON el ejercicio de la persona. No los implementes; deja stubs.

- `tests/test_file_handler.py` — El topic pide TDD/pruebas: este archivo es el ejercicio.
- `tests/test_filter.py` — El topic pide TDD/pruebas: este archivo es el ejercicio.

## Lo que le falta a este proyecto

Esto NO lo tenes que adivinar: salio de comparar el proyecto contra la arquitectura declarada del reto y de un analisis estatico del codigo. Completalo TODO.

### Boilerplate del stack que falta

Sin esto no compila ni arranca. Es andamiaje, no toca nada de lo pedagogico:

- **__init__.py** — Sin __init__.py, app no es un paquete importable y "import app.main" falla.

### Archivos que la arquitectura del reto declara y no estan

Creálos con implementacion real, en la capa que les corresponde:

- `data/output.txt`

## Como saber que terminaste

```bash
pip install -r requirements.txt && python -c "import app.main"
```

Ese comando corriendo sin errores es la definicion de "listo".

---

```
## Briefing del reto (autoridad)
Este bloque manda sobre los archivos adjuntos. El stack y el rol salen de AQUÍ, no de un topic genérico ni de markdown placeholder.

### Contexto técnico original
Hacer un programa simple con Python

### Reto
- Tema: Python
- Seniority: trainee-l2
- Tipo: practical
- Título: Implementación de un programa básico en Python
- Tiempo estimado: 2 horas

### Fases (trabajo del HUMANO — PROHIBIDO completarlas)
No implementes estos entregables. Dejalos como hueco pedagógico. El asistente solo materializa el proyecto arrancable para que el participante pueda trabajar.
- Fase 1: Lectura y escritura de archivos — objetivo: Implementar la lectura de un archivo de texto y escribir las líneas filtradas en un nuevo archivo. — entregable (NO resolver): Programa que lee un archivo de texto, filtra líneas con la palabra 'Python' y escribe en un nuevo archivo.
- Fase 2: Mejora y refactorización — objetivo: Mejorar el programa para que sea más eficiente y manejar más casos de error. — entregable (NO resolver): Programa refactorizado que maneja más casos de error y es más eficiente.

Eres un asistente experto en análisis, corrección y generación de archivos de cualquier tipo:
código fuente, documentación, hojas de cálculo, documentos Word, configuraciones, entre otros.
Voy a enviarte una cadena de texto que contiene uno o más archivos. Cada archivo está delimitado por un marcador con el siguiente formato:
// === ARCHIVO: ruta/del/archivo.extension ===
o también puede aparecer como:
## === ARCHIVO: ruta/del/archivo.extension ===
Lo que sigue al marcador puede ser:

El contenido real del archivo (código, texto, YAML, etc.)
Una descripción en lenguaje natural de lo que debe contener el archivo


TU TAREA
PASO 0 — ¿Esto es un proyecto o una carcasa?
Antes de extraer archivos, leé el Briefing (si está) y diagnosticá el adjunto.

Es CARCASA si ocurre CUALQUIERA de estas:
- No hay manifiesto de dependencias del stack del briefing (manifest.json de VTEX IO / package.json / pom.xml / build.gradle / requirements.txt / go.mod / *.tf / *.csproj, según corresponda)
- Hay un "binario" que en realidad es un comentario ("no puede ser mostrado como texto plano", placeholder .fig/.docx vacío)
- Los markdowns ya completan entregables de fases posteriores ("se implementó fade-in", lista de áreas ya resuelta)

Si es CARCASA:
- MATERIALIZÁ un proyecto que arranca en el stack del briefing (VTEX IO Store Framework, Angular, Terraform, pytest, Nest, etc.). Incluí manifiesto, punto de entrada y capa de interfaz reales.
- NO copies los markdowns de "solución" como si fueran el producto. Son ruido de generación.
- NO resuelvas las fases del briefing (están marcadas PROHIBIDO). Dejá el hueco pedagógico: el flujo existe, las microinteracciones/calidad/infra que el reto pide NO están hechas.
- Después seguí al PASO 5 (ZIP).

Si es un proyecto REAL (manifiesto + código que compila o arranca):
- Seguí PASO 1 en adelante. 🔴 compilación sí. 🟡 pedagógico no.

PASO 1 — Detección y extracción
Identifica todos los archivos presentes en la cadena. Para cada archivo extrae:

Su ruta completa (ej: src/main/java/com/pragma/Service.java)
Su contenido o descripción

PASO 2 — Clasificación por tipo
Clasifica cada archivo en una de estas categorías:
A) Código fuente (Java, Python, TypeScript, JavaScript, Kotlin, etc.)
B) Configuración / documentación (YAML, properties, Markdown, JSON, txt, etc.)
C) Excel (.xlsx, .xls, .csv)
D) Word (.docx, .doc)
E) Otro tipo de archivo binario o especial
PASO 3 — Clasificación de errores en código fuente

Objetivo prioritario: que el proyecto compile. No corrijas flujo de negocio ni lógica funcional.

Antes de modificar cualquier archivo de código fuente, clasifica cada problema encontrado en una de estas dos categorías:
🔴 ERROR DE COMPILACIÓN — corregir siempre
Son errores que impiden que el proyecto arranque, sin valor pedagógico:

Import faltante o incorrecto
Clase, método o variable referenciada que no existe en ningún archivo del proyecto
Error de sintaxis
Anotación con atributos inválidos
Dependencia ausente en pom.xml, package.json, etc.
Archivo referenciado que no existe y debe ser creado con implementación mínima

→ CORREGIR estos errores.
🟡 PROBLEMA FUNCIONAL O DE CALIDAD — preservar siempre
Son problemas que no impiden compilar. Pueden ser intencionales para el aprendizaje:

Clave secreta hardcodeada ("secret", "password123")
API deprecada que funciona pero tiene reemplazo moderno
Lógica de negocio incorrecta o incompleta
Código redundante o de baja legibilidad
Falta de validaciones en flujo de negocio
Patrones de diseño incorrectos pero funcionales
Concurrencia no segura
Configuración funcional pero no óptima

→ PRESERVAR tal cual. No corregir, no mejorar, no comentar.
PASO 4 — Procesamiento según tipo de archivo
Tipo A — Código fuente
Aplica únicamente las correcciones clasificadas como 🔴 ERROR DE COMPILACIÓN.
No alteres ningún elemento clasificado como 🟡 PROBLEMA FUNCIONAL O DE CALIDAD.
Si falta un archivo referenciado, créalo con la implementación mínima necesaria para compilar.
Tipo B — Configuración / documentación
Extrae el contenido tal cual, sin modificaciones salvo errores evidentes de sintaxis
(ej: YAML mal indentado).
Tipo C — Excel (.xlsx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un archivo Excel funcional con:

Fila de encabezados en negrita con color de fondo distintivo
Columnas con ancho ajustado al contenido
Tipos de dato correctos por columna
Validaciones si la descripción lo indica
Hojas nombradas descriptivamente si hay más de una
Filas de ejemplo si no hay datos reales

Tipo D — Word (.docx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un documento Word funcional con:

Estilos de título (Título 1, Título 2) para jerarquía de secciones
Fuente legible (Calibri o equivalente), tamaño 11-12pt para cuerpo
Márgenes estándar
Tabla de contenido si tiene múltiples secciones
Tablas con encabezados en negrita si aplica

Tipo E — Otro
Genera el archivo con el contenido o estructura más apropiada según la descripción.
PASO 5 — Exportación en ZIP
Empaqueta todos los archivos en un único archivo ZIP descargable respetando exactamente
la estructura de rutas indicada por los marcadores.
El ZIP debe incluir:

Archivos de código con únicamente los errores de compilación corregidos
Archivos de configuración y documentación sin cambios
Archivos nuevos creados para resolver dependencias de compilación faltantes
Archivos Excel y Word generados desde descripción

IMPORTANTE: El ZIP debe estar listo para descargar al finalizar. No preguntes si el usuario
quiere generarlo. Simplemente genera el archivo y proporciona el enlace de descarga; No debes desplegar en el chat el resumen de lo que arreglaste al Zip, solo entregalo.

REGLAS IMPORTANTES

No omitas ningún archivo aunque no tenga errores ni modificaciones
Respeta los nombres y rutas exactas indicadas por los marcadores
Si un archivo no tiene marcador claro, infiere el nombre desde su contenido
Si la cadena contiene solo documentación, placeholders o binarios fake, NO la reproduzcas:
aplicá PASO 0 (materializar el proyecto del briefing). Reproducir la carcasa es un fallo.
No agregues texto después del enlace de descarga del ZIP
No preguntes si el usuario quiere el ZIP: simplemente generalo siempre
Si detectas que falta un archivo de configuración necesario para compilar
(pom.xml, package.json, requirements.txt, build.gradle, etc.), créalo e inclúyelo
inferiendo su contenido desde los imports y frameworks detectados en el código
Nunca corrijas problemas 🟡 aunque parezcan obvios o fáciles de mejorar.
El participante que recibirá este proyecto los debe encontrar y resolver él mismo.


INPUT
Aquí está la cadena con los archivos:

// === ARCHIVO: requirements.txt ===
pytest==8.2.0

// === ARCHIVO: src/main.py ===
import os
from file_handler import read_file, write_file
from filter import filter_lines

def main():
    input_file = "data/input.txt"
    output_file = "data/output.txt"
    keyword = "Python"
    
    try:
        # Leer el archivo de entrada
        lines = read_file(input_file)
        
        # Filtrar líneas que contienen la palabra clave
        filtered_lines = filter_lines(lines, keyword)
        
        # Escribir las líneas filtradas en el archivo de salida
        write_file(output_file, filtered_lines)
        
        print(f"Proceso completado. Se escribieron {len(filtered_lines)} líneas en {output_file}")
    except FileNotFoundError:
        print(f"Error: El archivo {input_file} no existe.")
    except PermissionError:
        print(f"Error: No tienes permisos para leer {input_file} o escribir en {output_file}.")
    except Exception as e:
        print(f"Error inesperado: {str(e)}")

if __name__ == "__main__":
    # Verificar que el directorio data existe
    if not os.path.exists("data"):
        os.makedirs("data")
    
    # Crear un archivo input.txt de ejemplo si no existe
    if not os.path.exists("data/input.txt"):
        with open("data/input.txt", "w", encoding="utf-8") as f:
            f.write("Este es un ejemplo de archivo de texto.\n")
            f.write("Python es un lenguaje de programación poderoso.\n")
            f.write("Aprender Python es esencial para desarrolladores.\n")
            f.write("Este archivo será procesado por el programa.\n")
            f.write("La palabra clave es Python.\n")
    
    main()

// === ARCHIVO: __init__.py ===
# Paquete raíz del proyecto Python básico
# Permite que el directorio sea importable como un paquete Python
// === ARCHIVO: README.md ===
# Proyecto: Filtro de Líneas en Python

## Descripción

Aplicación de línea de comandos que lee un archivo de texto, filtra las líneas que contienen una palabra específica y guarda el resultado en un nuevo archivo.

## Estructura del Proyecto

```
proyecto/
├── __init__.py              # Paquete raíz
├── requirements.txt         # Dependencias del proyecto
├── src/
│   ├── __init__.py         # Paquete src
│   ├── main.py             # Punto de entrada
│   ├── file_handler.py     # Módulo de lectura/escritura
│   └── filter.py           # Módulo de filtrado
├── data/
│   ├── input.txt          # Archivo de entrada
│   └── output.txt         # Archivo de salida
└── tests/
    ├── __init__.py        # Paquete de tests
    ├── test_file_handler.py
    └── test_filter.py
```

## Requisitos Previos

- Python 3.12 o superior
- pip (gestor de paquetes de Python)

## Instalación

1. Crear un entorno virtual (recomendado):
   ```bash
   python -m venv venv
   ```

2. Activar el entorno virtual:
   - En Windows:
     ```bash
     venv\Scripts\activate
     ```
   - En Linux/macOS:
     ```bash
     source venv/bin/activate
     ```

3. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Uso Básico

### Ejecución Directa

El programa se ejecuta desde el directorio raíz del proyecto:

```bash
python -m src.main
```

Por defecto, esto procesará `data/input.txt` y escribirá el resultado en `data/output.txt`, filtrando las líneas que contengan la palabra "Python".

### Ejecución con Argumentos

Puedes especificar archivos de entrada y salida personalizados:

```bash
python -m src.main --input data/mi_archivo.txt --output data/resultado.txt --filter "palabra"
```

Argumentos disponibles:
- `--input` o `-i`: Ruta al archivo de entrada (por defecto: `data/input.txt`)
- `--output` o `-o`: Ruta al archivo de salida (por defecto: `data/output.txt`)
- `--filter` o `-f`: Palabra a filtrar en las líneas (por defecto: "Python")

### Ejecución como Script

```bash
python src/main.py
```

## Ejemplos de Uso

### Ejemplo 1: Uso básico

Contenido de `data/input.txt`:
```
Este es un archivo de prueba.
Python es un lenguaje de programación.
Aprendiendo Python es divertido.
Otro lenguaje popular es Java.
Python aparece múltiples veces en este texto.
```

Ejecutar:
```bash
python -m src.main
```

Contenido de `data/output.txt`:
```
Python es un lenguaje de programación.
Aprendiendo Python es divertido.
Python aparece múltiples veces en este texto.
```

### Ejemplo 2: Filtrar palabra personalizada

```bash
python -m src.main --filter "Java"
```

Esto filtrará solo las líneas que contengan "Java".

### Ejemplo 3: Archivos personalizados

```bash
python -m src.main -i datos/entrada.txt -o resultados/salida.txt -f "test"
```

## Ejecución de Pruebas

El proyecto incluye pruebas unitarias para los módulos principales.

### Ejecutar todas las pruebas

```bash
pytest
```

### Ejecutar pruebas de un módulo específico

```bash
pytest tests/test_file_handler.py
pytest tests/test_filter.py
```

### Ejecutar pruebas converbose

```bash
pytest -v
```

### Ver cobertura de pruebas

```bash
pytest --cov=src
```

## Manejo de Errores

El programa maneja los siguientes casos de error:

- **Archivo de entrada no encontrado**: Muestra un mensaje claro y sale con código de error 1
- **Permisos insuficientes**: Informa al usuario sobre problemas de lectura/escritura
- **Archivo de salida en directorio no existente**: Crea los directorios necesarios automáticamente

Ejemplo de mensaje de error:
```
Error: El archivo 'data/input.txt' no existe.
Por favor, crea el archivo o especifica otro路径 con --input
```

## Arquitectura

El proyecto sigue una arquitectura modular con separación de responsabilidades:

- **src/file_handler.py**: Encargado de la lectura y escritura de archivos utilizando context managers (`with`) para garantizar el cierre automático de archivos.
- **src/filter.py**: Contiene la lógica de filtrado de líneas según el criterio especificado.
- **src/main.py**: Punto de entrada que orquesta el flujo completo y maneja los argumentos de línea de comandos.

## Convenciones de Código

- Nombres de funciones y variables en `snake_case`
- Uso de `with` para manejo de archivos
- Manejo de errores con bloques `try-except` específicos
- Docstrings en formato estándar de Python

## Contribuir

1. Fork del repositorio
2. Crear una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit de tus cambios (`git commit -am 'Agrega nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crear un Pull Request

## Licencia

Este proyecto es de uso educativo.

// === ARCHIVO: src/file_handler.py ===
"""Módulo dedicado a operaciones de lectura y escritura de archivos.

Este módulo proporciona funciones utilitarias para manejar operaciones
de entrada/salida de archivos de texto con manejo robusto de errores.
"""

from typing import List, Optional
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def read_file(file_path: str) -> List[str]:
    """Lee todas las líneas de un archivo de texto.
    
    Args:
        file_path: Ruta al archivo a leer.
        
    Returns:
        Lista de líneas del archivo sin el caracter de salto de línea.
        
    Raises:
        FileNotFoundError: Si el archivo no existe.
        PermissionError: Si no hay permisos de lectura.
        IOError: Para otros errores de lectura.
    """
    lines = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            logger.info(f"Se leyeron {len(lines)} líneas del archivo {file_path}")
    except FileNotFoundError:
        logger.error(f"El archivo '{file_path}' no fue encontrado")
        raise
    except PermissionError:
        logger.error(f"No se tienen permisos de lectura para '{file_path}'")
        raise
    except IOError as e:
        logger.error(f"Error de E/S al leer '{file_path}': {str(e)}")
        raise
    
    return [line.rstrip('\n') for line in lines]


def write_file(file_path: str, lines: List[str]) -> int:
    """Escribe una lista de líneas en un archivo de texto.
    
    Args:
        file_path: Ruta al archivo donde escribir.
        lines: Lista de líneas a escribir.
        
    Returns:
        Número de líneas escritas.
        
    Raises:
        PermissionError: Si no hay permisos de escritura.
        IOError: Para otros errores de escritura.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            for line in lines:
                file.write(line + '\n')
            logger.info(f"Se escribieron {len(lines)} líneas en el archivo {file_path}")
    except PermissionError:
        logger.error(f"No se tienen permisos de escritura para '{file_path}'")
        raise
    except IOError as e:
        logger.error(f"Error de E/S al escribir en '{file_path}': {str(e)}")
        raise
    
    return len(lines)


def read_file_safe(file_path: str, default: Optional[List[str]] = None) -> List[str]:
    """Lee un archivo de forma segura, retornando un valor por defecto si falla.
    
    Args:
        file_path: Ruta al archivo a leer.
        default: Valor a retornar si ocurre un error. Por defecto es lista vacía.
        
    Returns:
        Lista de líneas del archivo o el valor por defecto.
    """
    if default is None:
        default = []
    
    try:
        return read_file(file_path)
    except (FileNotFoundError, PermissionError, IOError) as e:
        logger.warning(f"Error al leer archivo '{file_path}': {str(e)}")
        return default


def file_exists(file_path: str) -> bool:
    """Verifica si un archivo existe.
    
    Args:
        file_path: Ruta al archivo a verificar.
        
    Returns:
        True si el archivo existe, False en caso contrario.
    """
    import os
    return os.path.isfile(file_path)


def get_file_info(file_path: str) -> dict:
    """Obtiene información básica de un archivo.
    
    Args:
        file_path: Ruta al archivo.
        
    Returns:
        Diccionario con información del archivo (existe, tamaño, líneas).
    """
    import os
    
    info = {
        'exists': False,
        'size': 0,
        'line_count': 0
    }
    
    if not file_exists(file_path):
        return info
    
    info['exists'] = True
    
    try:
        info['size'] = os.path.getsize(file_path)
        lines = read_file(file_path)
        info['line_count'] = len(lines)
    except (IOError, PermissionError) as e:
        logger.warning(f"No se pudo obtener información completa: {str(e)}")
    
    return info


// === ARCHIVO: src/filter.py ===
"""Módulo dedicado al filtrado de líneas según palabra clave.

Este módulo proporciona funciones para filtrar líneas de texto
que contengan una palabra específica, con soporte para diferentes
modos de búsqueda y opciones de configuración.
"""

from typing import List, Callable, Optional
import logging

logger = logging.getLogger(__name__)


def filter_lines(lines: List[str], keyword: str, case_sensitive: bool = True) -> List[str]:
    """Filtra líneas que contengan una palabra clave específica.
    
    Args:
        lines: Lista de líneas a filtrar.
        keyword: Palabra clave a buscar en cada línea.
        case_sensitive: Si True, la búsqueda distingue mayúsculas de minúsculas.
        
    Returns:
        Lista de líneas que contienen la palabra clave.
    """
    if not keyword:
        logger.warning("Se proporcionó una palabra clave vacía")
        return lines.copy()
    
    filtered_lines = []
    
    for line in lines:
        if case_sensitive:
            if keyword in line:
                filtered_lines.append(line)
        else:
            if keyword.lower() in line.lower():
                filtered_lines.append(line)
    
    logger.info(f"Filtradas {len(filtered_lines)} líneas con la palabra '{keyword}' "
                f"(case_sensitive={case_sensitive})")
    
    return filtered_lines


def filter_lines_with_predicate(
    lines: List[str], 
    predicate: Callable[[str], bool]
) -> List[str]:
    """Filtra líneas usando una función predicado personalizada.
    
    Args:
        lines: Lista de líneas a filtrar.
        predicate: Función que recibe una línea y retorna True si debe incluirse.
        
    Returns:
        Lista de líneas que cumplen el predicado.
    """
    filtered_lines = [line for line in lines if predicate(line)]
    logger.info(f"Filtradas {len(filtered_lines)} líneas usando predicado personalizado")
    return filtered_lines


def filter_lines_containing_any(
    lines: List[str], 
    keywords: List[str], 
    case_sensitive: bool = True
) -> List[str]:
    """Filtra líneas que contengan cualquiera de las palabras clave.
    
    Args:
        lines: Lista de líneas a filtrar.
        keywords: Lista de palabras clave a buscar.
        case_sensitive: Si True, la búsqueda distingue mayúsculas de minúsculas.
        
    Returns:
        Lista de líneas que contienen al menos una palabra clave.
    """
    if not keywords:
        logger.warning("Se proporcionó una lista vacía de palabras clave")
        return []
    
    filtered_lines = []
    
    for line in lines:
        for keyword in keywords:
            if case_sensitive:
                if keyword in line:
                    filtered_lines.append(line)
                    break
            else:
                if keyword.lower() in line.lower():
                    filtered_lines.append(line)
                    break
    
    logger.info(f"Filtradas {len(filtered_lines)} líneas con cualquiera de "
                f"las palabras: {keywords}")
    
    return filtered_lines


def filter_lines_excluding(
    lines: List[str], 
    keyword: str, 
    case_sensitive: bool = True
) -> List[str]:
    """Filtra líneas EXCLUYENDO las que contengan la palabra clave.
    
    Args:
        lines: Lista de líneas a filtrar.
        keyword: Palabra clave a excluir.
        case_sensitive: Si True, la búsqueda distingue mayúsculas de minúsculas.
        
    Returns:
        Lista de líneas que NO contienen la palabra clave.
    """
    if not keyword:
        logger.warning("Se proporcionó una palabra clave vacía")
        return lines.copy()
    
    filtered_lines = []
    
    for line in lines:
        if case_sensitive:
            if keyword not in line:
                filtered_lines.append(line)
        else:
            if keyword.lower() not in line.lower():
                filtered_lines.append(line)
    
    logger.info(f"Excluidas {len(lines) - len(filtered_lines)} líneas con la palabra '{keyword}'")
    
    return filtered_lines


def count_keyword_occurrences(lines: List[str], keyword: str) -> int:
    """Cuenta las ocurrencias de una palabra clave en todas las líneas.
    
    Args:
        lines: Lista de líneas a analizar.
        keyword: Palabra clave a buscar.
        
    Returns:
        Número total de ocurrencias de la palabra clave.
    """
    if not keyword:
        return 0
    
    count = 0
    for line in lines:
        count += line.lower().count(keyword.lower())
    
    logger.info(f"Se encontraron {count} ocurrencias de '{keyword}'")
    return count


def get_matching_lines_with_context(
    lines: List[str], 
    keyword: str, 
    context_lines: int = 1,
    case_sensitive: bool = True
) -> List[tuple]:
    """Obtiene líneas que coinciden con la palabra clave junto con líneas de contexto.
    
    Args:
        lines: Lista de líneas a analizar.
        keyword: Palabra clave a buscar.
        context_lines: Número de líneas de contexto a incluir antes y después.
        case_sensitive: Si True, la búsqueda distingue mayúsculas de minúsculas.
        
    Returns:
        Lista de tuplas (número_de_línea, línea).
    """
    matches = []
    
    for idx, line in enumerate(lines):
        contains_keyword = (keyword in line) if case_sensitive \
                          else (keyword.lower() in line.lower())
        
        if contains_keyword:
            start = max(0, idx - context_lines)
            end = min(len(lines), idx + context_lines + 1)
            
            for context_idx in range(start, end):
                matches.append((context_idx + 1, lines[context_idx]))
    
    logger.info(f"Se encontraron {len(matches)} líneas con contexto para '{keyword}'")
    return matches


// === ARCHIVO: data/input.txt ===
Welcome to the Python programming course! This is a comprehensive guide for beginners.
In this module, we will explore the fundamental concepts of Python development.
The Python language is known for its simplicity and readability.
This text file is used as test data for the filtering program.
Learning Python opens many doors in the software industry.
Python was created by Guido van Rossum in the late 1980s.
The program will filter lines containing the word Python and write them to output.txt.
Many developers prefer Python for data analysis and machine learning tasks.
This is a sample file with multiple lines of text for testing purposes.
Python supports multiple programming paradigms including procedural and OOP.
The filter functionality demonstrates basic file handling in Python.
Understanding file I/O operations is essential for any Python developer.
Python has a vast ecosystem of libraries and frameworks.
This line does not contain the keyword we are searching for.
Python is widely used in scientific computing and research.
The main function will read this file and process each line systematically.
Error handling is an important aspect of robust Python programs.
Python's syntax emphasizes code readability and reduces program complexity.
Here is another line without the target word for testing the filter.
Python continues to be one of the most popular programming languages worldwide.
The file_handler module provides functions for reading and writing files safely.
Using context managers (with statements) ensures proper resource management.
Python's standard library includes many modules for common programming tasks.
This is additional content to ensure the file has sufficient test data.
The filter module contains the logic for identifying lines with specific keywords.
Developing strong fundamentals in Python is crucial for career growth in tech.
Python's dynamic typing and interpreted nature make it great for rapid prototyping.
This line is included to add more variety to the test dataset.
Modules and functions in Python promote code reuse and modular design.
The program demonstrates the integration of multiple components working together.
Python's community is known for being welcoming and supportive of newcomers.
Understanding how to work with files is a fundamental skill for programmers.
This final line completes our sample input file with diverse content.
// === ARCHIVO: data/output.txt ===


// === ARCHIVO: tests/test_file_handler.py ===
import pytest
from src import file_handler


class TestFileHandler:
    """Tests para el módulo de manejo de archivos."""

    @pytest.mark.skip(reason="Superficie de práctica - implementar por el estudiante")
    def test_leer_archivo_existente(self):
        """Verifica que se puede leer un archivo que existe."""
        # Given: un archivo de texto existente
        # When: se llama a la función de lectura
        # Then: retorna las líneas del archivo
        pass

    @pytest.mark.skip(reason="Superficie de práctica - implementar por el estudiante")
    def test_leer_archivo_inexistente(self):
        """Verifica el comportamiento cuando el archivo no existe."""
        # Given: una ruta a un archivo que no existe
        # When: se intenta leer el archivo
        # Then: lanza FileNotFoundError
        pass

    @pytest.mark.skip(reason="Superficie de práctica - implementar por el estudiante")
    def test_escribir_archivo(self):
        """Verifica que se pueden escribir líneas en un archivo."""
        # Given: una lista de líneas y una ruta de destino
        # When: se llama a la función de escritura
        # Then: el archivo se crea con el contenido esperado
        pass

    @pytest.mark.skip(reason="Superficie de práctica - implementar por el estudiante")
    def test_escribir_en_directorio_sin_permisos(self):
        """Verifica el comportamiento cuando no hay permisos de escritura."""
        # Given: una ruta sin permisos de escritura
        # When: se intenta escribir el archivo
        # Then: lanza PermissionError
        pass

    @pytest.mark.skip(reason="Superficie de práctica - implementar por el estudiante")
    def test_archivo_vacio(self):
        """Verifica el comportamiento con un archivo vacío."""
        # Given: un archivo que existe pero está vacío
        # When: se lee el archivo
        # Then: retorna una lista vacía
        pass


// === ARCHIVO: tests/test_filter.py ===
import pytest
from src import filter


class TestFilter:
    """Tests para el módulo de filtrado de líneas."""

    @pytest.mark.skip(reason="Superficie de práctica - implementar por el estudiante")
    def test_filtrar_lineas_con_palabra_exacta(self):
        """Verifica que se filtran líneas que contienen la palabra exacta."""
        # Given: una lista de líneas y la palabra "Python"
        # When: se aplica el filtro
        # Then: solo se retornan las líneas que contienen "Python"
        pass

    @pytest.mark.skip(reason="Superficie de práctica - implementar por el estudiante")
    def test_filtrar_sin_coincidencias(self):
        """Verifica el comportamiento cuando ninguna línea coincide."""
        # Given: una lista de líneas sin la palabra buscada
        # When: se aplica el filtro
        # Then: retorna una lista vacía
        pass

    @pytest.mark.skip(reason="Superficie de práctica - implementar por el estudiante")
    def test_filtrar_todas_coinciden(self):
        """Verifica el comportamiento cuando todas las líneas coinciden."""
        # Given: una lista donde todas las líneas contienen la palabra
        # When: se aplica el filtro
        # Then: retorna todas las líneas
        pass

    @pytest.mark.skip(reason="Superficie de práctica - implementar por el estudiante")
    def test_filtrar_lineas_vacias(self):
        """Verifica que las líneas vacías se manejan correctamente."""
        # Given: una lista con líneas vacías
        # When: se aplica el filtro
        # Then: las líneas vacías no se incluyen en el resultado
        pass

    @pytest.mark.skip(reason="Superficie de práctica - implementar por el estudiante")
    def test_filtrar_distingue_mayusculas_minusculas(self):
        """Verifica si el filtro distingue entre mayúsculas y minúsculas."""
        # Given: líneas con "python", "Python", "PYTHON"
        # When: se busca "Python"
        # Then: comportamiento según lo implementado
        pass

```
