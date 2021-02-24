import pandas as pd


file = '/Users/aviralmehrotra/Downloads/Code/MTF/2020-2021/Vaccination Simulation/Voronoi/codingTable.csv'

df = pd.read_csv(file)

nodes = df['Node'].tolist()
population = df['Population'].tolist()
caseRates = df['Case Rate'].tolist()
vaccinationRates = df['Vaccination Rate'].tolist()
ratios = df['Ratio'].tolist()

i = 0
remainingPopulation = sum(population)

while remainingPopulation > 0.5:
    zipped = sorted(zip(caseRates, nodes, population, vaccinationRates, ratios))

    caseRates = [w for (w, x, y, z, z1) in zipped]
    nodes = [x for (w, x, y, z, z1) in zipped]
    population = [y for (w, x, y, z, z1) in zipped]
    vaccinationRates = [z for (w, x, y, z, z1) in zipped]
    ratios = [z1 for (w, x, y, z, z1) in zipped]

    nodes.reverse()
    caseRates.reverse()
    population.reverse()
    vaccinationRates.reverse()
    ratios.reverse()

    for j in range(10): # Example with 10 active nodes
        population[j] -= ((vaccinationRates[j] * 0.9995) + caseRates[j])
        remainingPopulation -= ((vaccinationRates[j] * 0.9995) + caseRates[j])

        caseRates[j] = ratios[j] * (population[j] + (vaccinationRates[j] * 0.9995) + caseRates[j])

    for k in range(10, 66): # Example with 56 inactive nodes
        population[k] -= caseRates[k]
        remainingPopulation -= caseRates[k]

        caseRates[k] = ratios[k] * (population[k] + caseRates[k])

    i += 1

print('Total Number of Weeks for Every Person to be Vaccinated:', i)

