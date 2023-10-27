import read_csv
import charts
import utils

def run():
    data = read_csv.read_csv('./data.csv')
    data = list(filter(lambda item: item['Continent'] == 'South America', data))

    countries = list(map(lambda x: x['Country/Territory'], data))
    percentages = list(map(lambda x: x['World Population Percentage'], data))
    charts.generate_pie_chart(countries, percentages)

    country = input('Type Country => ').capitalize()
    result = utils.populationByCountry(data, country)

    if len(result) > 0:
        country = result[0]
        labels, values = utils.getPopulation(country)
        charts.generate_bar_chart(labels, values)

if __name__ == '__main__':
    run()