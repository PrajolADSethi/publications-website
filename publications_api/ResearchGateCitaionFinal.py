import urllib.error
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup
import pprint

faculty = ["Shilpa_Sonawani", "Mangesh_Bedekar", "Pradnya_Kulkarni5"]


def find_articles(author):
    url = "https://www.researchgate.net/profile/" + author
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    names = []
    title = []

    for div in soup.findAll('a', {'class': 'nova-e-link nova-e-link--color-inherit nova-e-link--theme-bare'}):
        names.append(div.text.strip())

    for name in names:
        p = name.split()
        if len(p) > 3:
            title.append(name)

    return title


def find_article_links(i):
    url = "https://www.researchgate.net/profile/" + i
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    links = []

    for div in soup.findAll('a', {
        'class': 'nova-c-button nova-c-button--align-center nova-c-button--radius-m nova-c-button--size-s '
                 'nova-c-button--color-blue nova-c-button--theme-bare nova-c-button--width-auto '
                 'nova-v-publication-item__action'}):
        links.append(div.get('href', None))

    return links


def find_citation(i):
    url = "https://www.researchgate.net/profile/" + i
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    citation_count = []

    for div in soup.findAll('div', {
        'class': 'nova-e-text nova-e-text--size-xl nova-e-text--family-sans-serif nova-e-text--spacing-none '
                 'nova-e-text--color-inherit'}):
        citation_count.append(div.text.strip())

    return citation_count[2]


def individual_citation(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")

    indiv_citation = []

    for h in soup.findAll('h2', {'class': "nova-e-text nova-e-text--size-m nova-e-text--family-sans-serif "
                                          "nova-e-text--spacing-none nova-e-text--color-inherit"}):
        indiv_citation.append(h.contents)
    temp = indiv_citation[0][0]
    # return indiv_citation[0][0]
    return int(
        ((((temp.split()[1]).split("("))[1]).split(")")[0]).split("'")[0])



def get_researchgate_data(author):
    pubs = find_articles(author)
    art_links = find_article_links(author)

    current_pub = 0
    for i in art_links:

        # ------------ ADD ALL INFO TO DB using pubs[current_pub] to get the specific title from db ------------

        print(individual_citation(i))
        current_pub+=1
