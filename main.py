import read_data as rd
import utils

if __name__ == '__main__':
    data = rd.read_csv('D:/python/reto1/world_population.csv')

    continents = ['Asia', 'Africa', 'North America',
                  'South America', 'Europe', 'Oceania', ]
    option = 1
    countries = []
    pop_rates = []
    while option <= len(continents) and option > 0:
        print('1. Asia | 2. Africa | 3. North America | 4. South America | 5. Europe | 6. Oceania | 0. Exit\n')
        option = int(input('Choose continent that  you want to graph: '))
        if option == 0:
            break
        countries, pop_rates = utils.get_population(
            data, continents[option - 1])
        utils.graph_pie_chart(countries, pop_rates)
