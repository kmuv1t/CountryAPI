import sys
import requests


def request(url):
    try:
        ans = requests.get(url)
        if ans.status_code == 200:
            return ans.json()  # Parsing
    except:
        print(f'Error, unable to request from {url}.')


def number_of_countries():
    ans = request(f'https://restcountries.com/v3.1/all')
    if ans:
        return len(ans)


def list_countries():
    ans = request(f'https://restcountries.com/v3.1/all')
    for country in ans:
        print(f"{country['name']['common']} - {country['region']}")


def show_population(name):
    ans = request(f'https://restcountries.com/v3.1/name/{name}')
    if ans:
        for country in ans:
            print(f"{country['name']['common']}: {country['population']}")
    else:
        print('Country not found.')


def show_currency(currency):
    ans = request(f'https://restcountries.com/v3.1/currency/{currency}')
    if ans:
        for country in ans:
            print(f"Currencies in {country['name']['common']}:")
            for cur in country['currencies']:
                print(f"{cur} - {country['currencies'][cur]['symbol']} - {country['currencies'][cur]['name']}")
    else:
        print('Currency not found.')


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('-'*50)
        print('|         Welcome to country system API          |')
        print('-'*50)
        print('Usage: python main.py <action> <complement>\n'
              'Actions -> help, list, count, currency, population\n'
              'Complement -> <country_name> or <currency>')
    else:
        if sys.argv[1] == 'list':
            print(list_countries())
        elif sys.argv[1] == 'count':
            print(f'There are currently {number_of_countries()} countries.')
        elif sys.argv[1] == 'currency':
            try:
                show_currency(sys.argv[2])
            except:
                print('You need to pass the desired country.')
        elif sys.argv[1] == 'population':
            try:
                show_population(sys.argv[2])
            except:
                print('You need to pass the desired country.')
        elif sys.argv[1] == 'help':
            print(f"list - Lists all countries in the world and their respective regions.\n"
                  f"count - Returns how many countries there are currently.\n"
                  f"currency <currency> - Returns all currencies used in the respective country.\n"
                  f"population <country_name> - Returns country population number.")
        else:
            print('Invalid parameter.')
