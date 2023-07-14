from modules.book import Book
from modules.magazine import Magazine
from modules.dvd import Dvd
from modules.cd import Cd
from modules.catalog import Catalog
import json
book1 =Book(
    'Title Test',
    'ini subject Test',
    None,
    '1345-5433',
    'Satyaki',
    '082122365180'
)
book2 =Book(
    'test 1',
    'ini subject Test1',
    None,
    '1345-5434',
    'Satyaki1',
    '082122365181'
)
magazine1 = Magazine(
    'test 245',
    'edisi 14 Juli 2023',
    None,
    'volume 2',
    '-'
)
magazine2 = Magazine(
    'media 123',
    'edisi 14 Juli 2023',
    None,
    'volume 3',
    '-'
)
dvd1 = Dvd(
    'test DVD 1',
    None,
    'Subect 1',
    'Tom Cruis',
    "nolan",
    'comedy'
)
cd = Cd(
    'test 123',
    None,
    'subject123',
    'artist123'
)
#collect data per jenis
book = [book1,book2]
magazine = [magazine1,magazine2]
dvd = [dvd1]
cd = [cd]
#get data from json
f = open('files/catalog.json')
data_json = json.load(f)

#create object from data json
for item in data_json:
    if item['source'] == 'book':
        book.append(Book(
            title=item['title'],
            upc=item['upc'],
            subject=item['subject'],
            isbn=item['isbn'],
            authors=item['authors'],
            dbs_number=item['dbs_number']
        ))
    elif item['source'] == 'magazine':
        magazine.append(Magazine(
            title=item['title'],
            upc=item['upc'],
            subject=item['subject'],
            volume=item['volume'],
            issue=item['issue'],
        ))
    elif item['source'] == 'cd':
        cd.append(Cd(
            title=item['title'],
            upc=item['upc'],
            subject=item['subject'],
            artist=item['artist']
        ))  
    elif item['source'] == 'dvd':
        dvd.append(Dvd(
            title=item['title'],
            upc=item['upc'],
            subject=item['subject'],
            actor=item['actor'],
            director=item['director'],
            genre = item['genre']
        )
        )


#collect all data
catalog_all = [book,magazine,dvd,cd]

#input search
input_search = 'test'
results = Catalog(catalog_all).search(input_search)
if results:
    for index, result in enumerate(results):
        print(f'result ke -{index+1}|{result}')

else:
    print("no result")