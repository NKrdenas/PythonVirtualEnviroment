import read_csv
import charts
import world
import utils


# def run():
#     data = read_csv.read_csv('C:/Users/ncard/Platzi/Python 102/app/data.csv')
#     country = input('Type Country => ').capitalize()
#     result = utils.populationByCountry(data, country)

#     if len(result) > 0:
#         country = result[0]
#         labels, values = utils.getPopulation(country)
#         charts.generate_bar_chart(labels, values)
    
#     print(result)
#POBLACION DE CADA PAIS POR AñOS

def run():
    data = read_csv.read_csv('C:/Users/ncard/Platzi/Python 102/app/data.csv')
    data = list(filter(lambda item: item['Continent'] == 'South America', data))

    countries = list(map(lambda x: x['Country/Territory'], data))
    percentages = list(map(lambda x: x['World Population Percentage'], data))
    charts.generate_pie_chart(countries, percentages)

if __name__ == '__main__':
    run()