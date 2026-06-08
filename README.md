# Projeto 5 - Algoritmos Genéticos (Otimização de Função Real)

Este projeto consiste na implementação de um Algoritmo Genético (AG) para encontrar o valor máximo da função matemática $f(x) = x^2 - 3x + 4$ no intervalo $X = [-10, +10]$, conforme solicitado na atividade prática da disciplina.

## Estrutura do Projeto

- **algoritmo_genetico_tp05.py**: Script principal contendo a implementação do AG (codificação, decodificação, seleção, crossover e mutação).
- **relatorio_tecnico_algoritmos_geneticos.pdf**: Relatório técnico detalhando a metodologia, parâmetros utilizados e análise dos resultados.

## Funcionalidades

### Representação e Decodificação
- **Genótipo**: Cromossomos representados por cadeias de bits (binário puro).
- **Fenótipo**: Mapeamento linear do valor binário para o intervalo real $[-10, 10]$ do problema.
- **Resolução**: A variável $L$ (quantidade de bits) define a granularidade da busca no espaço contínuo.

### Operadores Genéticos
- **Seleção por Torneio**: Combate direto entre indivíduos para definir os progenitores.
- **Crossover de Ponto Único**: Taxa de 70% para recombinação de genes entre os pais.
- **Mutação Bit-flip**: Taxa de 1% de chance de inversão de bit para manter a diversidade genética.
- **Elitismo**: Estratégia para garantir a preservação do melhor indivíduo de cada geração.

## Parâmetros (Versão de Submissão)

Para atender aos requisitos mínimos do enunciado, o script está configurado por padrão com:
- `POP_SIZE = 4`
- `NUM_GENERATIONS = 5`
- `BIT_LENGTH (L) = 5`
- `CROSSOVER_RATE = 0.7`
- `MUTATION_RATE = 0.01`

*(Testes avançados com $L=12$, população 8 e 20 gerações foram realizados para análise de estabilidade).*

## Como Executar

1. **Instalar dependências**:
   Este projeto utiliza apenas bibliotecas base do Python (ou NumPy, caso instalado):
   ```bash
   pip install numpy
   ```
2. **Executar o projeto**:
    ```
    python algoritmo_genetico_tp05.py
    ```

## Resultados Esperados

O algoritmo exibe no console:
- O melhor indivíduo de cada geração (Valor de X, Fitness e Representação Binária).
- O resumo final com a melhor solução encontrada após todas as gerações.
- Geralmente converge para valores próximos de $x \approx -10$ (ponto de máximo no intervalo dado).

## Conclusão

O projeto valida que a escolha dos hiperparâmetros (como o número de bits e o tamanho da população) é crucial para equilibrar a precisão numérica e a estabilidade da convergência em problemas de otimização estocástica.

## Autores

- Lucas de Oliveira Pereira  
- Renan Augusto Da Silva

## Link para o vídeo de explicação
