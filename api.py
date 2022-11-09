from fastapi import FastAPI, Request
from datetime import datetime

storage = FastAPI(title='My Fast Api')

@storage.get('/')
def index():
    return "My name is Gustave, This is my API here"

@storage.get('/today')
def today():
    return str(datetime.now())

@storage.get('/mynames')
def names(first_name: bool = True, last_name: bool = True):
    full_names = ""
    if first_name:
        full_names += 'Gustave'
    if last_name:
        full_names += ' Mbonyinshuti'

    return full_names



# if __name__ == '__main__':
#         app.run()


