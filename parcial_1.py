#esteDado un conjunto de puntos en un plano cartesiano, se te pide encontrar los dos puntos más cercanos entre sí. 
#Implementa una función llamada pares_cercanos que tome una lista de coordenadas (puntos en el plano) y devuelva las coordenadas de los dos
#puntos más cercanos junto con su distancia. Utiliza el algoritmo "Divide y Vencerás" para resolver problema de manera eficiente, 
#este ejercicio deberá usar Decoradores, como args y kwargs.

#Se importa math para hacer operaciones maematicas basicas
import math

def distancia(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def pares_cercanos_divide_y_venceras(coordenadas):
    n = len(coordenadas)
    
    # Caso base: Si hay 3 puntos o menos, calculamos distancias directamente
    if n <= 3:
        min_dist = float('inf')
        puntos_mas_cercanos = ()
        for i in range(n):
            for j in range(i + 1, n):
                dist = distancia(coordenadas[i], coordenadas[j])
                if dist < min_dist:
                    min_dist = dist
                    puntos_mas_cercanos = (coordenadas[i], coordenadas[j])
        return puntos_mas_cercanos, min_dist

    # Dividimos el conjunto en dos mitades
    medio = n // 2
    coordenadas_izquierda = coordenadas[:medio]
    coordenadas_derecha = coordenadas[medio:]

    # Llamamos recursivamente a la función en las mitades izquierda y derecha
    pares_izquierda, dist_izquierda = pares_cercanos_divide_y_venceras(coordenadas_izquierda)
    pares_derecha, dist_derecha = pares_cercanos_divide_y_venceras(coordenadas_derecha)

    # Encontramos la distancia mínima entre las mitades izquierda y derecha
    min_dist = min(dist_izquierda, dist_derecha)
    
    # Combinamos los resultados de las mitades
    puntos_mas_cercanos = pares_izquierda if dist_izquierda <= dist_derecha else pares_derecha

    # Creamos una franja con puntos cercanos al eje vertical medio
    strip = [punto for punto in coordenadas if abs(punto[0] - coordenadas[medio][0]) < min_dist]
    strip.sort(key=lambda x: x[1])

    # Buscamos puntos más cercanos en la franja
    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if strip[j][1] - strip[i][1] < min_dist:
                dist = distancia(strip[i], strip[j])
                if dist < min_dist:
                    min_dist = dist
                    puntos_mas_cercanos = (strip[i], strip[j])

    return puntos_mas_cercanos, min_dist

def encontrar_pares_cercanos(*args, **kwargs):
    coordenadas = args[0]
    coordenadas.sort(key=lambda x: x[0])  # Ordenamos las coordenadas por coordenada x
    return pares_cercanos_divide_y_venceras(coordenadas)



# Ejemplo de uso
# coordenadas = [(1, 2), (3, 5), (8, 9), (10, 11), (15, 17)]
# coordenadas = [(10, 20), (15, 17), (80, 90), (40, 11), (34, 51)]
coordenadas = [(120, 220), (515, 517), (480, 490), (240, 211), (434, 451)]
puntos_mas_cercanos, distancia_minima = encontrar_pares_cercanos(coordenadas)
print("Puntos más cercanos:", puntos_mas_cercanos)
print("Distancia mínima:", distancia_minima)
