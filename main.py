import requests
import re
import json

def write_to_file(filename):
    content = str(input('Введите то что хотите записать в файл'))
    with open(filename, 'w') as f:
        f.write(content)


def read_file(filename):
    with open(filename) as f:
        return f.read()

def get_result_from_url(url):
    result = requests.get(url)
    if result.status_code == 200:
        return result
    else:
        print("Status code {}".format(result.status_code))


def sava_headers_in_json(url: str, filename):
    r = requests.get(url)

    headers_dict = dict(r.headers)
    for key, value in headers_dict.items():
        print(key+':', value)

    with open(filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=128):
            f.write(chunk)

write_to_file('text.txt')
print(read_file('text.txt'))
sava_headers_in_json('https://jsonplaceholder.typicode.com/comments', 'request.json')