sourcesList = [
    {
        'category': 'sports',
        'name': 'Globo esporte',
        'url': 'https://ge.globo.com/'
    },
    {
        'category': 'culture',
        'name': 'G1 Pop e arte',
        'url': 'https://g1.globo.com/pop-arte/'
    }
]


def getSource(category):
    return [x for x in sourcesList if x['category'] == category]
