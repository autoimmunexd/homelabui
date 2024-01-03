import requests
from bs4 import BeautifulSoup

def scrape_wikipedia_main_page():
    url = "https://en.wikipedia.org/wiki/Main_Page"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the target div
        target_div = soup.find('div', {'id': 'mp-itn', 'class': 'mp-contains-float'})

        # Check if the target div is found
        if target_div:
            # Convert the target div to a string
            div_string = target_div
            print(type(div_string))
            return div_string
        else:
            print("Div not found on the page.")
    else:
        print("Failed to retrieve the webpage. Status code:", response.status_code)