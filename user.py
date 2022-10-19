from main import AsyncHTTPRequest

urls = [
    'https://www.',
    'https://www.',
    'https://www.',
]

with AsyncHTTPRequest() as ahttp:
    for url in urls:
        ahttp.get(url)