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