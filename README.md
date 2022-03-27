# Nodos_Arboles
Es un programa donde se muestran arboles y nodos con su respectiva profindidad.😊
python-dijkstra
El algoritmo de Dijkstra es un algoritmo para encontrar las rutas más cortas entre nodos en un gráfico ponderado.

Contenido
¿Cómo usar el módulo dijksta?
Encuentra todas las distancias y caminos
Encuentra el camino más corto
Encuentra la distancia más corta
Dibujar gráficos
¿Cómo usar el módulo dijksta?
Debe mostrar su gráfico como una matriz de adyacencia. Por ejemplo, observe este gráfico con su matriz de adyacencia:

Carreras de resistencia Carreras de resistencia

Tenga en cuenta que al usar la indexación de Python obtiene a = 0, b = 1 ... g = 6, z = 7

Descargue el módulo dijkstra.py y cópielo en su espacio de trabajo

Encuentra todas las distancias y caminos
dijstra . find_all ( wmat , inicio , fin = - 1 ):
Devuelve una tupla con una lista de distancias y una lista de rutas de todos los vértices restantes con la misma indexación.

    (distances, paths)
Por ejemplo, las distancias[x] son ​​las distancias más cortas desde el vértice x cuyo camino más corto es caminos[x]. x es un elemento de {0, 1, ..., n-1} donde n es el número de vértices

Args:
wmat    --  weighted graph's adjacency matrix
start   --  paths' first vertex
end     --  (optional) path's end vertex. Return just the 
            distance and its path

Exceptions:
Index out of range, Be careful with start and end vertices.
Código de ejemplo
import  dijkstra  # Importar el módulo

# Matriz de adyacencia ponderada 
wmat  = [[ 0 , 2 , 0 , 0 , 0 , 1 , 0 , 0 ],
        [ 2 , 0 , 2 , 2 , 4 , 0 , 0 , 0 ],
        [ 0 , 2 , 0 , 0 , 3 , 0 , 0 , 1 ],
        [ 0 , 2 , 0 , 0 , 4 , 3 , 0 , 0 ],
        [ 0 , 4 , 3 , 4 , 0 , 0 , 7 , 0 ],
        [ 1 , 0 , 0 , 3 , 0 , 0 , 5 , 0 ],
        [ 0 , 0 , 0 , 0 , 7 , 5 , 0 , 6 ],
        [ 0 , 0 , 1 , 0 , 0 , 0 , 6 , 0 ]]

imprimir ( dijkstra . find_all ( wmat , 0 ))
Producción:

([0, 2, 4, 4, 6, 1, 6, 5], [[0], [0, 1], [0, 1, 2], [0, 5, 3], [0, 1, 4], [0, 5], [0, 5, 6], [0, 1, 2, 7]])
Encuentra el camino más corto
dijstra . find_shortest_path ( wmat , start , end = - 1 ):
Devuelve la lista de caminos de todos los vértices restantes.

Args:
wmat    --  weighted graph's adjacency matrix
start   --  paths' first vertex
end     --  (optional) path's end vertex. Return just
            the path

Exceptions:
Index out of range, Be careful with start and end vertices.
Código de ejemplo con vértice final
import  dijkstra  # Importar el módulo

# Matriz de adyacencia ponderada 
wmat  = [[ 0 , 2 , 0 , 0 , 0 , 1 , 0 , 0 ],
        [ 2 , 0 , 2 , 2 , 4 , 0 , 0 , 0 ],
        [ 0 , 2 , 0 , 0 , 3 , 0 , 0 , 1 ],
        [ 0 , 2 , 0 , 0 , 4 , 3 , 0 , 0 ],
        [ 0 , 4 , 3 , 4 , 0 , 0 , 7 , 0 ],
        [ 1 , 0 , 0 , 3 , 0 , 0 , 5 , 0 ],
        [ 0 , 0 , 0 , 0 , 7 , 5 , 0 , 6 ],
        [ 0 , 0 , 1 , 0 , 0 , 0 , 6 , 0 ]]

imprimir ( dijkstra . find_shortest_path ( wmat , 0 , 7 ))
Producción:

[0, 1, 2, 7]
Código de ejemplo sin vértice final
import  dijkstra  # Importar el módulo

# Matriz de adyacencia ponderada 
wmat  = [[ 0 , 2 , 0 , 0 , 0 , 1 , 0 , 0 ],
        [ 2 , 0 , 2 , 2 , 4 , 0 , 0 , 0 ],
        [ 0 , 2 , 0 , 0 , 3 , 0 , 0 , 1 ],
        [ 0 , 2 , 0 , 0 , 4 , 3 , 0 , 0 ],
        [ 0 , 4 , 3 , 4 , 0 , 0 , 7 , 0 ],
        [ 1 , 0 , 0 , 3 , 0 , 0 , 5 , 0 ],
        [ 0 , 0 , 0 , 0 , 7 , 5 , 0 , 6 ],
        [ 0 , 0 , 1 , 0 , 0 , 0 , 6 , 0 ]]

imprimir ( dijkstra . find_shortest_path ( wmat , 0 ))
Producción:

[[0], [0, 1], [0, 1, 2], [0, 5, 3], [0, 1, 4], [0, 5], [0, 5, 6], [0, 1, 2, 7]]
Encuentra la distancia más corta
dijstra . find_shortest_distance ( wmat , inicio , fin = - 1 ):
Devuelve la lista de distancias de todos los vértices restantes.

Args:
wmat    --  weighted graph's adjacency matrix
start   --  paths' first vertex
end     --  (optional) path's end vertex. Return just
            the distance

Exceptions:
Index out of range, Be careful with start and end vertices.
Código de ejemplo con vértice final
import  dijkstra  # Importar el módulo

# Matriz de adyacencia ponderada 
wmat  = [[ 0 , 2 , 0 , 0 , 0 , 1 , 0 , 0 ],
        [ 2 , 0 , 2 , 2 , 4 , 0 , 0 , 0 ],
        [ 0 , 2 , 0 , 0 , 3 , 0 , 0 , 1 ],
        [ 0 , 2 , 0 , 0 , 4 , 3 , 0 , 0 ],
        [ 0 , 4 , 3 , 4 , 0 , 0 , 7 , 0 ],
        [ 1 , 0 , 0 , 3 , 0 , 0 , 5 , 0 ],
        [ 0 , 0 , 0 , 0 , 7 , 5 , 0 , 6 ],
        [ 0 , 0 , 1 , 0 , 0 , 0 , 6 , 0 ]]

imprimir ( dijkstra . find_shortest_distance ( wmat , 0 , 7 ))
Producción:

5
Código de ejemplo sin vértice final
import  dijkstra  # Importar el módulo

# Matriz de adyacencia ponderada 
wmat  = [[ 0 , 2 , 0 , 0 , 0 , 1 , 0 , 0 ],
        [ 2 , 0 , 2 , 2 , 4 , 0 , 0 , 0 ],
        [ 0 , 2 , 0 , 0 , 3 , 0 , 0 , 1 ],
        [ 0 , 2 , 0 , 0 , 4 , 3 , 0 , 0 ],
        [ 0 , 4 , 3 , 4 , 0 , 0 , 7 , 0 ],
        [ 1 , 0 , 0 , 3 , 0 , 0 , 5 , 0 ],
        [ 0 , 0 , 0 , 0 , 7 , 5 , 0 , 6 ],
        [ 0 , 0 , 1 , 0 , 0 , 0 , 6 , 0 ]]

imprimir ( dijkstra . find_shortest_distance ( wmat , 0 ))
Producción:

[0, 2, 4, 4, 6, 1, 6, 5]
Dibujar gráficos
Para obtener una representación visual usando la matriz de adyacencia, puede usar el siguiente módulo draw_graph.py

dibujar_grafo . gráfico_no_directo ( wmat , nombre = "gráfico_no_directo_ponderado" )
Crea un archivo pdf con la visualización del gráfico ponderado. Debes tener instalado graphviz (Python conector y compilación OS)

Sistema operativo: https://www.graphviz.org/

Módulo de Python: https://graphviz.readthedocs.io/en/stable/index.html

Args:
wmat  --  weigthted graph's adjacency matrix
name  --  (optional) graph's filenma
Código de ejemplo
import  draw_graph  # Importar el módulo

# Matriz de adyacencia ponderada 
wmat  = [[ 0 , 2 , 0 , 0 , 0 , 1 , 0 , 0 ],
        [ 2 , 0 , 2 , 2 , 4 , 0 , 0 , 0 ],
        [ 0 , 2 , 0 , 0 , 3 , 0 , 0 , 1 ],
        [ 0 , 2 , 0 , 0 , 4 , 3 , 0 , 0 ],
        [ 0 , 4 , 3 , 4 , 0 , 0 , 7 , 0 ],
        [ 1 , 0 , 0 , 3 , 0 , 0 , 5 , 0 ],
        [ 0 , 0 , 0 , 0 , 7 , 5 , 0 , 6 ],
        [ 0 , 0 , 1 , 0 , 0 , 0 , 6 , 0 ]]

imprimir ( dibujar_gráfico . gráfico_no dirigido ( wmat ))
