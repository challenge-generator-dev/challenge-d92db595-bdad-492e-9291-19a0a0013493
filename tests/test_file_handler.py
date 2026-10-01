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