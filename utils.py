import matplotlib.pyplot as plt

def get_population(data, continent):
    data = list(filter(lambda item: item['Continent'] == continent, data))
    countries = [country['Country/Territory'] for country in data]
    pop_rates = [float(rate['World Population Percentage']) for rate in data]
    
    return countries, pop_rates

def graph_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.show()