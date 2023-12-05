import requests
from bs4 import BeautifulSoup

def get_news_text(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find and extract text from relevant HTML tags (e.g., <p>)
        text_elements = soup.find_all('p')

        # Combine the extracted text into a single string
        news_text = ' '.join([element.get_text() for element in text_elements])

        return news_text
    else:
        # If the request was unsuccessful, print an error message
        print(f"Error: Unable to fetch content from {url}. Status code: {response.status_code}")
        return None

# Example usage
if __name__ == "__main__":
    # Replace this URL with the URL of the news article you want to scrape
    news_url = input("Input news URL: ")
    
    # Get the news text from the specified URL
    news_text = get_news_text(news_url)

    if news_text:
        print(news_text)
