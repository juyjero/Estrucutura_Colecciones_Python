# ==========================================
# SISTEMA DE GESTIÓN DE INVENTARIO (NIVEL INTERMEDIO)
# ==========================================

# 1. COLECCIONES Y MATRICES (Datos iniciales)
# Diccionario para buscar precios rápidamente por ID de producto
precios_productos = {
    101: 15.50,  # Producto: Camiseta
    102: 25.00,  # Producto: Pantalón
    103: 45.00,  # Producto: Zapatos
    104: 10.00   # Producto: Gorra
}

# Matriz (Lista de listas) que representa el stock en diferentes sucursales
# Formato: [ID_Producto, Stock_Sucursal_A, Stock_Sucursal_B]
matriz_inventario = [
    [101, 50, 30],
    [102, 20, 15],
    [103, 10, 12],
    [104, 100, 80]
]

# 2. FUNCIONES DEL SISTEMA

def calcular_stock_total(matriz):
    """
    Calcula el stock total de cada producto sumando todas las sucursales.
    Retorna un diccionario con el ID como clave y el stock total como valor.
    """
    totales = {}
    for fila in matriz:
        id_prod = fila[0]
        # Operador aritmético (+) para sumar el stock de ambas sucursales
        stock_total = fila[1] + fila[2]
        totales[id_prod] = stock_total
    return totales


def generar_alerta_reabastecimiento(matriz, limite_minimo=20):
    """
    Filtra qué productos están en estado crítico en alguna sucursal.
    Usa operadores lógicos y de comparación.
    """
    alertas = []
    for fila in matriz:
        id_prod = fila[0]
        # Operadores de comparación (<) y lógico (or)
        if fila[1] < limite_minimo or fila[2] < limite_minimo:
            alertas.append(id_prod)
    return alertas


def calcular_valor_inventario(precios, stocks_totales):
    """
    Multiplica el stock total por el precio para obtener el valor monetario.
    """
    valor_total = 0.0
    print("\n--- VALORACIÓN DE INVENTARIO ---")
    for id_prod, stock in stocks_totales.items():
        # Operador de membresía (in) para verificar si el ID existe en los precios
        if id_prod in precios:
            precio = precios[id_prod]
            # Operadores aritméticos (*) y de asignación compuesta (+=)
            valor_producto = stock * precio
            valor_total += valor_producto
            print(f"Producto ID {id_prod}: {stock} unidades x ${precio:.2f} = ${valor_producto:.2f}")
    
    return valor_total


# 3. FUNCIÓN PRINCIPAL (Flujo del programa)
def main():
    print("=== BIENVENIDO AL SISTEMA DE INVENTARIO INTERMEDIO ===")
    
    # Paso 1: Procesar la matriz para obtener totales
    totales = calcular_stock_total(matriz_inventario)
    
    # Paso 2: Evaluar alertas con operadores lógicos
    alertas = generar_alerta_reabastecimiento(matriz_inventario, limite_minimo=25)
    
    # Paso 3: Calcular costos totales
    valor_total_tienda = calcular_valor_inventario(precios_productos, totales)
    
    # 4. SALIDA DE RESULTADOS (Reporte Final)
    print("\n--- REPORTE FINAL DE ALERTAS ---")
    if len(alertas) > 0:
        print(f"⚠️ ¡Atención! Los siguientes IDs necesitan reabastecimiento urgente: {alertas}")
    else:
        print
