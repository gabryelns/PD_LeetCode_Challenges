from bisect import bisect_right

class Solution(object):

    @staticmethod
    def maxValue(events, k):
        # Ordena os eventos pelo dia de término
        events.sort(key=lambda x: x[1])
    
        # Extrai os dias de término para facilitar a busca binária
        end_days = [event[1] for event in events]
    
        # Inicializa a tabela de programação dinâmica
        # dp[i][j] representa o valor máximo que pode ser obtido com os primeiros i eventos e j seleções
        n = len(events)
        dp = [[0] * (k + 1) for _ in range(n + 1)]
    
        for i in range(1, n + 1):
            start, end, value = events[i-1]
        
            # Encontra o último evento que não conflita com o evento atual
            last_non_conflict = bisect_right(end_days, start - 1, 0, i-1)
        
            for j in range(1, k + 1):
                # Escolha 1: Não selecionar o evento atual
                dp[i][j] = dp[i-1][j]
            
                # Escolha 2: Selecionar o evento atual e adicionar ao valor máximo obtido até o último evento não conflitante
                dp[i][j] = max(dp[i][j], dp[last_non_conflict][j-1] + value)
    
        # O valor máximo será o maior valor na última linha da tabela dp
        return dp[n][k]
    
