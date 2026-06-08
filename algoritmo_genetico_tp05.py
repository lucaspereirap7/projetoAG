import random

# Parâmetros variáveis (recomendados)
POP_SIZE = 4           # população inicial
MUTATION_RATE = 0.01   # probabilidade de mutação por bit
CROSSOVER_RATE = 0.7   # probabilidade de crossover
NUM_GENERATIONS = 5   # número de gerações 
BIT_LENGTH = 12        # comprimento do cromossomo em bits
TOURNAMENT_SIZE = 3    # tamanho do torneio
ELITISM = True         # preservar o melhor indivíduo entre gerações
SEED = None            # se quiser reprodutibilidade, coloque um inteiro

# Função para decodificar o vetor binário para real no intervalo [-10, 10]
def decode(individual):
    bitstring = "".join(str(bit) for bit in individual)
    value = int(bitstring, 2)  # 0 .. 2^L - 1
    max_int = 2**BIT_LENGTH - 1
    # mapeamento linear 0..max_int -> -10..10
    x = -10 + (value / max_int) * 20
    return x

# Função de fitness
def fitness(x):
    return x**2 - 3*x + 4

# Gerar indivíduo aleatório
def random_individual():
    return [random.randint(0, 1) for _ in range(BIT_LENGTH)]

# Seleção por torneio (k amostras)
def tournament_selection(population, fitnesses, k=TOURNAMENT_SIZE):
    k = max(2, min(k, len(population)))
    contestants = random.sample(range(len(population)), k)
    best_idx = contestants[0]
    for idx in contestants[1:]:
        if fitnesses[idx] > fitnesses[best_idx]:
            best_idx = idx
    return population[best_idx][:]  # retorna cópia

# Crossover de um ponto
def crossover(parent1, parent2):
    if random.random() < CROSSOVER_RATE:
        point = random.randint(1, BIT_LENGTH - 1)
        return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]
    return parent1[:], parent2[:]

# Mutação
def mutate(individual):
    return [bit if random.random() > MUTATION_RATE else 1 - bit for bit in individual]

# Algoritmo Genético Principal
def genetic_algorithm():
    if SEED is not None:
        random.seed(SEED)

    population = [random_individual() for _ in range(POP_SIZE)]

    for generation in range(NUM_GENERATIONS):

        decoded = [decode(ind) for ind in population]
        fitnesses = [fitness(x) for x in decoded]

        best_idx = fitnesses.index(max(fitnesses))
        print(f"Geração {generation+1}: Melhor x = {decoded[best_idx]:.6f}, Fitness = {fitnesses[best_idx]:.6f}, Melhor Indivíduo = {population[best_idx]}")

        new_population = []

        if ELITISM:
            new_population.append(population[best_idx][:])

        while len(new_population) < POP_SIZE:

            parent1 = tournament_selection(population, fitnesses)
            parent2 = tournament_selection(population, fitnesses)

            offspring1, offspring2 = crossover(parent1, parent2)

            offspring1 = mutate(offspring1)
            offspring2 = mutate(offspring2)
            new_population.extend([offspring1, offspring2])

        population = new_population[:POP_SIZE]

    decoded = [decode(ind) for ind in population]
    fitnesses = [fitness(x) for x in decoded]
    best_idx = fitnesses.index(max(fitnesses))
    print(f"\nMelhor solução encontrada: x = {decoded[best_idx]:.6f}, Fitness = {fitnesses[best_idx]:.6f}, Melhor Indivíduo = {population[best_idx]}")

if __name__ == "__main__":
    genetic_algorithm()