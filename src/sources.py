sourcesList = [
    {
        'category': 'sports',
        'name': 'Globo esporte',
        'url': 'https://ge.globo.com/'
    },
    {
        'category': 'polity',
        'name': 'Globo news',
        'url': ''
    },
    {
        'category': 'culture',
        'name': 'Globo culture',
        'url': ''
    }
]

def getSourceByCategory(category):
    return [x for x in sourcesList if x['category'] == category ]