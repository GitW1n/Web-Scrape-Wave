from bs4 import BeautifulSoup



def parse_page(page_content, object_type):
    soup = BeautifulSoup(page_content, 'html.parser')
    if object_type == "url":
        return extract_links(soup)
    if object_type == "headers":
        return extract_titles(soup)
    

def extract_links(soup):
    links = [a['href'] for a in soup.find_all('a', href=True)]
    return links
    
def extract_titles(soup):
    titles = [title.get_text() for title in soup.find_all(['h1', 'h2', 'h3'])]
    return titles