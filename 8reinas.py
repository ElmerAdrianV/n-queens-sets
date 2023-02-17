def problema_8_reinas(n):
    tablero = {i for i in range(n**2)}
    soluciones = list()
    poniendo_reinas_backtracking(tablero,set(),soluciones,n)
    return soluciones
    
def poniendo_reinas_backtracking(tablero_disponible,pos_reinas_p,soluciones,n):
    if len(pos_reinas_p) == n and not (pos_reinas_p in soluciones):
        soluciones.append(  pos_reinas_p )
    else:
        for pos in tablero_disponible:
            nuevos_ocupados = genera_ocupacion(pos,n)
            poniendo_reinas_backtracking(tablero_disponible-nuevos_ocupados , pos_reinas_p|{pos}, soluciones, n)
            

def genera_ocupacion(pos,n):
    return genera_diagonal_ocupado(pos,n) | genera_horizontal_ocupada(pos,n) | genera_vertical_ocupada(pos,n)

def genera_diagonal_ocupado(pos,n):
    x,y = pos//n, pos%n
    numDiagID = abs(x-y)
    numDiagDI = abs(y+x-(n-1))
    # llenando la diagonal de izqueirda a derecha
    startID = pos-(n+1)*x if x-y <= 0 else pos-(n+1)*(x-numDiagID)
    diagonalID = {startID+i*(n+1) for i in range(n-numDiagID)}
    # llenando la diagonal de izqueirda a derecha
    startDI = pos-(n-1)*x if x+y <= n-1 else pos-(n-1)*(x-numDiagDI)
    diagonalDI = {startDI+i*(n-1) for i in range(n-numDiagDI)}
    return diagonalID | diagonalDI
    
def genera_horizontal_ocupada(pos,n):
    return {i + pos-pos%n for i in range(n)} 

def genera_vertical_ocupada(pos,n):
    return {i*n + pos%n for i in range(n)}