import charts
import read_csv

def world_percentage(data):
    country =[]
    percentage =[]

    for info in data:
        country.append(info['Country/Territory'])
        percentage.append(info['World Population Percentage'])
    return country, percentage
