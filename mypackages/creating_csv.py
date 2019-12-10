import csv

list_of_capitals = {'Aland Islands':'Mariehamn',
'Albania':'Tirana',
'Andorra':'Andorra la Vella',
'Armenia':'Yerevan',
'Austria':'Vienna',
'Azerbaijan':'Baku',
'Belarus':'Minsk',
'Belgium':'Brussels',
'Bosnia and Herzegovina':'Sarajevo',
'Bulgaria':'Sofia',
'Croatia':'Zagreb',
'Cyprus':'Nicosia',
'Czech Republic':'Prague',
'Denmark':'Copenhagen',
'Estonia':'Tallinn',
'Faroe Islands':'Torshavn',
'Finland':'Helsinki',
'France':'Paris',
'Georgia':'Tbilisi',
'Germany':'Berlin',
'Gibraltar':'Gibraltar',
'Greece':'Athens',
'Guernsey':'Saint Peter Port',
'Hungary':'Budapest',
'Iceland':'Reykjavik',
'Ireland':'Dublin',
'Isle of Man':'Douglas',
'Italy':'Rome',
'Jersey':'Saint Helier',
'Kosovo':'Pristina',
'Latvia':'Riga',
'Liechtenstein':'Vaduz',
'Lithuania':'Vilnius',
'Luxembourg':'Luxembourg',
'Macedonia':'Skopje',
'Malta':'Valletta',
'Moldova':'Chisinau',
'Monaco':'Monaco',
'Montenegro':'Podgorica',
'Netherlands':'Amsterdam',
'Northern Cyprus':'North Nicosia',
'Norway':'Oslo',
'Poland':'Warsaw',
'Portugal':'Lisbon',
'Romania':'Bucharest',
'Russia':'Moscow',
'San Marino':'San Marino',
'Serbia':'Belgrade',
'Slovakia':'Bratislava',
'Slovenia':'Ljubljana',
'Spain':'Madrid',
'Svalbard':'Longyearbyen',
'Sweden':'Stockholm',
'Switzerland':'Bern',
'Turkey':'Ankara',
'Ukraine':'Kyiv',
'United Kingdom':'London',
'Vatican City':'Vatican City'}

with open('list_of_capitals.csv', 'w') as f:
    fieldnames = ['State', 'Capital']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    data = [dict(zip(fieldnames, [k, v])) for k, v in list_of_capitals.items()]
    writer.writerows(data)

import pandas

df = pandas.read_csv('list_of_capitals.csv')
# print(df)
df.to_csv("list_of_capitals.csv", index= False)





