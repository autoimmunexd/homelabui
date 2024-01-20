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
            pretty = str(target_div)
            file_name = 'static/data/wiki_news.html'
            with open(file_name, "w") as file:
                file.write(pretty)
                print('WIKI HTML SAVED!')
        else:
            print("Div not found on the page.")
    else:
        print("Failed to retrieve the webpage. Status code:", response.status_code)