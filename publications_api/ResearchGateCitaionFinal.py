import urllib.error
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup
import pprint

faculty = ["Shilpa_Sonawani", "Mangesh_Bedekar", "Pradnya_Kulkarni5"]


def find_articles(i):
    url = "https://www.researchgate.net/profile/" + i
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


def individual_citation(i):
    url = i
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


art_links = []


for each in faculty:
    # pprint.pprint(find_citation(each))
    #   print("------------------------------------------------------------------")
    # pprint.pprint(find_articles(each))
    #  print("------------------------------------------------------------------")
    temp_links = find_article_links(each)
    for k in temp_links:
        art_links.append(k)
    # pprint.pprint(find_article_links(each))
    # print("==================================================================="
    #       "==================================================================="
    #       "==================================================================")

# temp_links = ["https://www.researchgate.net/publication"
#               "/332381355_Improved_Logistic_Regression_Approach_in_Feature_Selection_for_EHR",
#               "https://www.researchgate.net/publication/311250199_Classification_problem_solving_using_multi"
#               "-objective_optimization_approach_and_local_search"]

for i in art_links:
    print(individual_citation(i))
