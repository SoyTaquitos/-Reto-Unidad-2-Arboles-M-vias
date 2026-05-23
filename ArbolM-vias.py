"""
Laboratorio: TDA Árbol M-Vías
ESTÁNDAR: PEP 8 / P.O.O.
"""

class NodoMVias:
    """Representa un nodo para un árbol M-Vías de orden 'M'."""

    def __init__(self, orden):
        self._orden = orden
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
    def get_dato(self, indice):
        return self._datos[indice]

    def set_dato(self, indice, valor):
        self._datos[indice] = valor

    def get_hijo(self, indice):
        return self._hijos[indice]

    def set_hijo(self, indice, nodo):
        self._hijos[indice] = nodo

    def es_hoja(self):
        """Verifica si el nodo no tiene ningún hijo asociado."""
        for hijo in self._hijos:
            if hijo is not None:
                return False
        return True
        
    def esta_lleno(self):
        """Verifica si el nodo ya tiene todos sus datos ocupados."""
        return None not in self._datos


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

    # ==========================================
    # MÉTODO ORDENAR (RECORRIDO IN-ORDEN M-VÍAS)
    # ==========================================
    def ordenar_inorden(self, nodo_actual=None, inicial=True):
        """
        Retorna una lista con los elementos del árbol ordenados de menor a mayor.
        Intercala la visita a los hijos con la lectura de los datos.
        """
        if inicial:
            nodo_actual = self._raiz
            
        if nodo_actual is None:
            return []

        resultado = []
        for i in range(self._orden - 1):
            # 1. Visitar el hijo izquierdo del dato actual
            resultado.extend(self.ordenar_inorden(nodo_actual.get_hijo(i), False))
            
            # 2. Extraer el dato actual si existe
            dato = nodo_actual.get_dato(i)
            if dato is not None:
                resultado.append(dato)
                
        # 3. Visitar el último hijo (el más a la derecha)
        resultado.extend(self.ordenar_inorden(nodo_actual.get_hijo(self._orden - 1), False))
        
        return resultado

    # ==========================================
    # MÉTODO DE BALANCEO (FILOSOFÍA AVL)
    # ==========================================
    def es_balanceado_avl(self, nodo_actual=None, inicial=True):
        """
        Verifica si el árbol cumple con el principio de balanceo (tipo AVL).
        La diferencia de altura entre CUALQUIERA de sus M ramas no debe ser > 1.
        """
        if inicial:
            nodo_actual = self._raiz
            
        if nodo_actual is None:
            return True, 0

        alturas = []
        # Calculamos la altura de cada hijo recursivamente
        for i in range(self._orden):
            hijo = nodo_actual.get_hijo(i)
            balanceado, altura_hijo = self.es_balanceado_avl(hijo, False)
            
            if not balanceado:
                return False, 0
            alturas.append(altura_hijo)

        # En un M-vías, la diferencia máxima entre la rama más alta y la más baja
        max_altura = max(alturas)
        min_altura = min(alturas)
        
        es_balanceado = (max_altura - min_altura) <= 1
        altura_actual = max_altura + 1
        
        return es_balanceado, altura_actual

    # ==========================================
    # MÉTODO ELIMINAR (BÁSICO M-VÍAS)
    # ==========================================
    def eliminar(self, dato_a_borrar):
        """Busca un dato en la raíz y lo elimina, reordenando el nodo."""
        if self._raiz is None:
            return False
            
        # Para este laboratorio, implementamos la eliminación en el nodo actual (hoja o raíz simple)
        for i in range(self._orden - 1):
            if self._raiz.get_dato(i) == dato_a_borrar:
                # Se encontró el dato, lo borramos (ponemos None)
                self._raiz.set_dato(i, None)
                self._desplazar_datos(self._raiz, i)
                return True
        return False

    def _desplazar_datos(self, nodo, indice_vacio):
        """Desplaza los elementos hacia la izquierda para llenar el hueco del dato eliminado."""
        for i in range(indice_vacio, self._orden - 2):
            siguiente_dato = nodo.get_dato(i + 1)
            nodo.set_dato(i, siguiente_dato)
        # Limpiamos la última posición
        nodo.set_dato(self._orden - 2, None)


if __name__ == "__main__":
    orden_arbol = 3
    mi_arbol_m = ArbolMVias(orden_arbol)
    
    # Instanciamos la raíz
    raiz = NodoMVias(orden_arbol)
    raiz.set_dato(0, 100)
    raiz.set_dato(1, 200)
    mi_arbol_m.raiz = raiz
    
    print("--- LABORATORIO: ÁRBOL M-VÍAS ---")
    print(f"Árbol instanciado con orden: {mi_arbol_m.orden}")
    
    # Prueba de In-orden (Ordenar)
    print(f"Datos ordenados (In-orden): {mi_arbol_m.ordenar_inorden()}")
    
    # Prueba de Balanceo (AVL)
    balanceado, altura = mi_arbol_m.es_balanceado_avl()
    print(f"¿Cumple balanceo tipo AVL?: {balanceado} (Altura: {altura})")
    
    # Prueba de Eliminación
    print("\nEliminando el 100...")
    mi_arbol_m.eliminar(100)
    print(f"Datos después de eliminar: {mi_arbol_m.raiz.datos}")