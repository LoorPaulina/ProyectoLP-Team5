# Hash utilizado para el grafo
grafo = {
  'A' => { 'B' => 1, 'C' => 4 },
  'B' => { 'A' => 1, 'C' => 2, 'D' => 5 },
  'C' => { 'A' => 4, 'B' => 2, 'D' => 1 },
  'D' => { 'B' => 5, 'C' => 1 }
}

# Implementar el algoritmo de Dijkstra
def dijkstra(grafo, inicio)
  distancias = {} # La distancia mínima conocida desde el inicio a cada nodo
  predecesores = {} # El camino para llegar a cada nodo
  nodos = grafo.keys # Lista de todos los nodos

  grafo.each do |nodo, _|
    distancias[nodo] = Float::INFINITY
    predecesores[nodo] = nil
  end

  distancias[inicio] = 0

  until nodos.empty?
    nodo_mas_cercano = nodos.min_by { |nodo| distancias[nodo] }
    nodos.delete(nodo_mas_cercano)

    grafo[nodo_mas_cercano].each do |vecino, peso|
      alt = distancias[nodo_mas_cercano] + peso
      if alt < distancias[vecino]
        distancias[vecino] = alt
        predecesores[vecino] = nodo_mas_cercano
      end
    end
  end

  { distancias: distancias, predecesores: predecesores }
end

# Llamar al algoritmo de Dijkstra desde el nodo 'A'
resultado = dijkstra(grafo, 'A')

# Mostrar resultados
puts "Distancias desde el nodo 'A':"
resultado[:distancias].each do |nodo, distancia|
  puts "Distancia a #{nodo}: #{distancia}"
end

puts "\nCaminos más cortos desde el nodo 'A':"
resultado[:predecesores].each do |nodo, predecesor|
  if predecesor
    camino = []
    actual = nodo
    while actual
      camino.unshift(actual)
      actual = resultado[:predecesores][actual]
    end
    puts "Camino a #{nodo}: #{camino.join(' -> ')}"
  end
end