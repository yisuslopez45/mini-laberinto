
# 0 = libre , 1 = muro , 2 = bonus , 3 penalizacion, 9 destino

laberinto = [
    [0,1,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,0],
    [0,1,0,1,0,1,0,1,0],
    [0,1,0,0,0,1,0,0,0],
    [0,1,0,0,0,1,1,0,1],
    [0,2,0,0,0,0,0,0,1],
    [1,0,1,1,1,3,1,0,1],
    [0,0,0,0,0,0,0,0,1],
    [0,1,1,1,1,1,1,0,9]   
]

test = {
    1 : '🧱',
    0 : '🟩',
    2 : '💎',
    3 : '🧨',
    9 : '🏁'
}

pos = [0, 0]
meta = (8,8)

total_costo = 0
coins_actual = 20

# Función de costo
def costo_celda(valor):
    if valor == 0:
        return 1
    elif valor == 2:
        return 0.25
    elif valor == 3:
        return 3
    elif valor == 9:
        return 0
    else:
        return float("inf")


# Imprimir tablero
def imprimir_tablero(lab, pos):
    print('COINS ACTUALES', coins_actual)
    for i in range(len(lab)):
        fila = []
        for j in range(len(lab[0])):
            if (i, j) == tuple(pos):
                fila.append('🧠')
            else:
                fila.append( test[lab[i][j]] )
        print(" ".join(fila))
    print()
    
# Juego
print("Bienvenido al juego del laberinto 🐭🎮")
print("Controles: w=arriba, s=abajo, a=izquierda, d=derecha")
imprimir_tablero(laberinto, pos)


while True:
    mov = input("Ingresa tu movimiento (w/a/s/d): ").strip().lower()
    if mov not in ["w", "a", "s", "d"]:
        print("Movimiento inválido.")
        continue

    # Calcular nueva posición
    nueva_pos = pos.copy()
    if mov == "w":
        nueva_pos[0] -= 1
    elif mov == "s":
        nueva_pos[0] += 1
    elif mov == "a":
        nueva_pos[1] -= 1
    elif mov == "d":
        nueva_pos[1] += 1

    # Validar movimiento
    x, y = nueva_pos
    if not (0 <= x < len(laberinto) and 0 <= y < len(laberinto[0])):
        print("No puedes salirte del tablero ❌")
        continue
    if laberinto[x][y] == 1:
        print("Choque con un muro 🚧")
        continue

    # Actualizar posición y costo
    pos = nueva_pos
    total_costo += costo_celda(laberinto[x][y])
    coins_actual -= costo_celda(laberinto[x][y])

    if coins_actual <= 0:
        print("☠️ ¡Has consumido todos tus coins!")
        break

    imprimir_tablero(laberinto, pos)

    # Verificar meta
    if tuple(pos) == meta:
        print("🎉 ¡Has llegado a la meta!")
        print(f"✅ Total de coins consumidos: {total_costo}")
        print(f"✅ Total de coins restantes: {coins_actual}")
        break
