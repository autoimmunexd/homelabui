import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_wikipedia_main_page():
    url = "https://en.wikipedia.org/wiki/Main_Page"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the target div
        target_div = soup.find('div', {'id': 'mp-itn', 'class': 'mp-contains-float'})

        # Check if the target div is found
        if target_div:
            # Find the div with the specified content and remove it
            to_remove = target_div.find('div', {'class': 'hlist itn-footer noprint', 'style': 'text-align:right;'})
            if to_remove:
                to_remove.decompose()

            # Find all div elements inside the target div
            div_elements = target_div.find_all('div', recursive=False)

            # Iterate through div elements to find and remove the one with the anchor link
            for div_element in div_elements:
                anchor_link = div_element.find('a', {'href': '/wiki/Wikipedia:In_the_news/Candidates', 'title': 'Wikipedia:In_the_news/Candidates'})
                if anchor_link:
                    div_element.decompose()

            # Insert the text "Last Updated" with the current date and time in 12-hour format
            current_time = datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")  # 12-hour format with AM/PM
            target_div.append(f'Last Updated: {current_time}')

            # Convert the soup to a string
            modified_html = str(target_div)
            file_name = 'static/data/wiki_news.html'

            # Write the modified HTML to a file
            with open(file_name, "w") as file:
                file.write(modified_html)

            print('WIKI HTML SAVED!')
        else:
            print("Div not found on the page.")
    else:
        print("Failed to retrieve the webpage. Status code:", response.status_code)

# Call the function to perform the scraping and modification
scrape_wikipedia_main_page()
