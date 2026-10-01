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