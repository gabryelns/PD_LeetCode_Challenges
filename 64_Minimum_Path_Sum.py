class Solution(object):
    def minPathSum(self, grid):
        
        m = len(grid)  # Número de linhas na grade
        n = len(grid[0])  # Número de colunas na grade
    
        # Inicializa o array de distâncias
        # dist[i][j] armazenará a soma mínima do caminho de (0, 0) até (i, j)
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = grid[0][0]  # A soma mínima para o ponto de partida é o valor da célula (0, 0)
    
        # Relaxamento das arestas utilizando o belman ford para a direita e para baixo em cada célula para encontrar o caminho mais curto.
        for i in range(m):
            for j in range(n):
                # Relaxamento para a célula abaixo (i+1, j)
                if i < m - 1:  # Verifica se a célula abaixo existe
                    dist[i+1][j] = min(dist[i+1][j], dist[i][j] + grid[i+1][j])
                    # Atualiza a distância mínima para a célula abaixo, se um caminho menor for encontrado
                
                # Relaxamento para a célula à direita (i, j+1)
                if j < n - 1:  # Verifica se a célula à direita existe
                    dist[i][j+1] = min(dist[i][j+1], dist[i][j] + grid[i][j+1])
                    # Atualiza a distância mínima para a célula à direita, se um caminho menor for encontrado
    
        # Retorna a soma mínima do caminho até a célula (m-1, n-1)
        return dist[m-1][n-1]
    