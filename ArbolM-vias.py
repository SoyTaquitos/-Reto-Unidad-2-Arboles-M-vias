"""
Laboratorio: TDA Árbol M-Vías
ESTÁNDAR: PEP 8 / P.O.O.
"""

class NodoMVias:
    """Representa un nodo para un árbol M-Vías de orden 'M'."""

    def __init__(self, orden):
        self._orden = orden
        # Un nodo M-vías tiene como máximo (M-1) datos y M hijos
        # Inicializamos las listas con valores nulos (None)
        self._datos = [None] * (orden - 1)
        self._hijos = [None] * orden

    # ==========================================
    # GETTERS Y SETTERS GLOBALES (@property)
    # ==========================================
    
    @property
    def orden(self):
        return self._orden

    @property
    def datos(self):
        return self._datos

    @datos.setter
    def datos(self, nuevos_datos):
        self._datos = nuevos_datos

    @property
    def hijos(self):
        return self._hijos

    @hijos.setter
    def hijos(self, nuevos_hijos):
        self._hijos = nuevos_hijos

    # ==========================================
    # GETTERS Y SETTERS ESPECÍFICOS (Por Índice)
    # ==========================================
    # En árboles M-vías es fundamental acceder a posiciones específicas
    
    def get_dato(self, indice):
        """Retorna el dato en una posición específica."""
        return self._datos[indice]

    def set_dato(self, indice, valor):
        """Asigna un valor en una posición específica."""
        self._datos[indice] = valor

    def get_hijo(self, indice):
        """Retorna el nodo hijo en una posición específica."""
        return self._hijos[indice]

    def set_hijo(self, indice, nodo):
        """Asigna un nodo hijo en una posición específica."""
        self._hijos[indice] = nodo

    def es_hoja(self):
        """Verifica si el nodo no tiene ningún hijo asociado."""
        for hijo in self._hijos:
            if hijo is not None:
                return False
        return True


class ArbolMVias:
    """Estructura de Datos Abstracta para la gestión del Árbol M-Vías."""

    def __init__(self, orden):
        self._orden = orden
        self._raiz = None

    @property
    def raiz(self):
        return self._raiz

    @raiz.setter
    def raiz(self, nodo):
        self._raiz = nodo
        
    @property
    def orden(self):
        return self._orden


if __name__ == "__main__":
    # Prueba del TDA: Crear un árbol de orden 3 (Ej: un árbol 2-3)
    # Por regla: tendrá máximo 2 datos y 3 hijos por nodo
    orden_arbol = 3
    mi_arbol_m = ArbolMVias(orden_arbol)
    
    # Instanciamos la raíz y usamos los setters específicos por índice
    raiz = NodoMVias(orden_arbol)
    raiz.set_dato(0, 100)
    raiz.set_dato(1, 200)
    
    # Asignamos la raíz al árbol usando el setter global
    mi_arbol_m.raiz = raiz
    
    # Demostración en consola
    print("--- LABORATORIO: ÁRBOL M-VÍAS ---")
    print(f"Árbol instanciado con orden: {mi_arbol_m.orden}")
    print(f"Datos almacenados en la raíz: {mi_arbol_m.raiz.datos}")
    print(f"Espacios para hijos en la raíz: {len(mi_arbol_m.raiz.hijos)}")
    print(f"¿La raíz actualmente es una hoja?: {mi_arbol_m.raiz.es_hoja()}")