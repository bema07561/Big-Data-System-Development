import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

def get_genre_page(genre_url):
    response = requests.get(genre_url)

    if response.status_code != 200:
        raise Exception('Failed to load page {}'.format(genre_url))

    genre_doc = BeautifulSoup(response.text, 'html.parser')
    return genre_doc


def genre_books_info(div_tags):
    # Tag for the Book Name
    Book_Name_tags = div_tags.find('span')

    # Tag for the Author's Name
    Author_Name_tags = div_tags.find(['a', 'span'], class_=['a-size-small a-link-child', 'a-size-small a-color-base'])

    # Book URL
    Book_URL = 'https://amazon.in' + div_tags.find('a', class_='a-link-normal')['href']

    # Tag for the Book Type
    Book_Type_tags = div_tags.find('span', class_='a-size-small a-color-secondary a-text-normal')

    # Tag for Book Price
    Price_tags = div_tags.find('span', class_='p13n-sc-price')

    # Tag for the number of stars
    Star_Rating_tags = div_tags.find('span', class_='a-icon-alt')

    # Tag for the number of reviews
    Reviews_tags = div_tags.find('div', class_='a-icon-row')

    return Book_Name_tags, Author_Name_tags, Book_URL, Book_Type_tags, Price_tags, Star_Rating_tags, Reviews_tags

def get_genre_books(genre_doc):
    div_selection_class = 'zg-grid-general-faceout'
    div_tags = genre_doc.find_all('div', class_=div_selection_class)
    # Creating dictionary of the book attributes
    genre_books_dict = {
        'Book_Name': [],
        'Author_Name': [],
        'Book_URL': [],
        'Book_Type': [],
        'Price': [],
        'Star_Rating': [],
        'Reviews': []
    }
    # Creating the list of book ttributes
    for i in range(0, len(div_tags)):
        genre_info = genre_books_info(div_tags[i])

        if genre_info[0] is not None:
            genre_books_dict['Book_Name'].append(genre_info[0].text)
        else:
            genre_books_dict['Book_Name'].append('Missing')

        if genre_info[1] is not None:
            genre_books_dict['Author_Name'].append(genre_info[1].text)
        else:
            genre_books_dict['Author_Name'].append('Missing')

        if genre_info[2] is not None:
            genre_books_dict['Book_URL'].append(genre_info[2])
        else:
            genre_books_dict['Book_URL'].append('Missing')

        if genre_info[3] is not None:
            genre_books_dict['Book_Type'].append(genre_info[3].text)
        else:
            genre_books_dict['Book_Type'].append('Missing')

        if genre_info[4] is not None:
            genre_books_dict['Price'].append(genre_info[4].text)
        else:
            genre_books_dict['Price'].append('Missing')

        if genre_info[5] is not None:
            genre_books_dict['Star_Rating'].append(genre_info[5].text)
        else:
            genre_books_dict['Star_Rating'].append('Missing')

        # Applying extra find as at the time of writing for one book reviews were not availabe
        if genre_info[6] is not None:
            genre_books_dict['Reviews'].append(genre_info[6].find('span', class_='a-size-small').text)
        else:
            genre_books_dict['Reviews'].append('Missing')
    return pd.DataFrame(genre_books_dict)

def scrape_genre(genre_ulr, path):
    # Stopping the function to create the already exiting file
    if os.path.exists(path):
        print('The file {} already exists.. Skipping...'.format(path))
        return
    # Creating dataframe with genre_titles and genre_urls columns
    genre_df = get_genre_books(get_genre_page(genre_ulr))
    # Saving the dataframe to csv format
    genre_df.to_csv(path, index=None)



def get_genre_info(doc):
    # Selecting a parent tag
    div_selection_class = '_p13n-zg-nav-tree-all_style_zg-browse-group__88fbz'
    genre_div_tags = doc.find_all('div', class_=div_selection_class)

    # Selecting a useful tag out of the parent tag
    genre_tags = genre_div_tags[0].find_all('a')

    # List for genre_titles
    genre_titles = []

    for i in range(0, len(genre_tags)):
        genre_titles.append(genre_tags[i].text)

    # List for genre_urls
    genre_urls = []
    base_url = 'https://www.amazon.in'

    for i in range(0, len(genre_tags)):
        genre_urls.append(base_url + genre_tags[i]['href'])
    return genre_titles, genre_urls


def scrape_genres():
    # Using request library to fetch the books genres
    genre_url = 'https://www.amazon.in/gp/bestsellers/books/'
    response = requests.get(genre_url)

    # Check the page requests success
    if response.status_code != 200:
        raise Exception('Failed to load page {}'.format(genre_url))

    # Creating a BeautifulSoup object
    doc = BeautifulSoup(response.text, 'html.parser')

    # Dictionary to which lists from get_genre_info are passed
    genre_dic = {
        'genre_titles': get_genre_info(doc)[0],
        'genre_urls': get_genre_info(doc)[1]
    }
    return pd.DataFrame(genre_dic)

def scrape_genre_books():
    print('Scraping list of book genres')
    # Scraping the genre_titles and genre_urls
    genres_df = scrape_genres()
    # Creating a 'data' folder
    os.makedirs('data', exist_ok = True)
    # Looping to extract the genre_title and the genre_url
    for index, row in genres_df.iterrows():
        print('Scraping bestselling books for the genre {}'. format(row['genre_titles']))
        # Inputing genre_url and path to save the file to scrape_genre.
        scrape_genre(row['genre_urls'], 'data/{}.csv'.format(row['genre_titles']))


if __name__ == '__main__':
    scrape_genre_books()
