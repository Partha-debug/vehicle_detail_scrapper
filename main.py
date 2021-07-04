import requests
from bs4 import BeautifulSoup
from states import places


def get_vehicle_details(number):
    query = f"{places[f'{number[0:2].lower()}'] + number[2:4].lower()}"
    url = f'https://www.drivespark.com/rto-vehicle-registration-details/{query}/'
    print(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    data = soup.find("div", {"class": "ds-bike-price-slider website-link"}).find_all('tr')[2::]

    parsed_data = {}

    for i in data:
        key = (str(*i.find_all('td')[0].text.split('\n')))
        value = str(*i.find_all('td')[1].text.split('\n')).replace('\r', '')
        parsed_data[key] = value

    return parsed_data

if __name__ == "__main__":

    test_number = 'OR05AQ6010'

    try:
        print(get_vehicle_details(test_number))
    except Exception as e:
        print(f"Some error occured, details: {e}")