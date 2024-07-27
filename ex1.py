countries = ['Russia', 'USA', 'UK','Germany']
capitals = ['Moscow', 'Washington', 'London', 'Berlin']
population = [145934462, 311022651, 80345321, 67886011]
for (co, ca, popul) in zip(countries, capitals, population):
     print(f'{ca} is the capital of {co}, population equal {popul} people.')