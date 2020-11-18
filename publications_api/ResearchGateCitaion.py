import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import pprint, time

faculty = ["Shilpa_Sonawani", ]

for i in faculty:
    url = "https://www.researchgate.net/profile/" + i
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    # print(html)

    persons = []
    titles = []
    links = []
    citations_per_art = []
    names = []
    link_cont = []

    for div in soup.findAll('a', {'class': 'nova-e-link nova-e-link--color-inherit nova-e-link--theme-bare'}):
        names.append(div.text.strip())

    for div in soup.findAll('a', {
        'class': 'nova-c-button nova-c-button--align-center nova-c-button--radius-m nova-c-button--size-s '
                 'nova-c-button--color-blue nova-c-button--theme-bare nova-c-button--width-auto '
                 'nova-v-publication-item__action'}):
        links.append(div.get('href', None))
        link_cont.append(div.contents)

    for div in soup.findAll('div', {
        'class': 'nova-e-text nova-e-text--size-xl nova-e-text--family-sans-serif nova-e-text--spacing-none '
                 'nova-e-text--color-inherit'}):
        # person[div.find('p').attrs['class'][0]] = div.text.strip()
        persons.append(div.text.strip())

    #     pprint.pprint(persons[2])
    #

    for name in names:
        p = name.split()
        if len(p) > 3:
            titles.append(name)

pprint.pprint(titles)
print(len(titles))

pprint.pprint(links)

for link in links:
    print("hello")
    # time.sleep(15)
    url = link
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
