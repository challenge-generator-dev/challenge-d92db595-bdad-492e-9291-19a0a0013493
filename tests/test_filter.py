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