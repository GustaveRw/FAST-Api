from fastapi import FastAPI

app = FastAPI(title='My Fast Api')

@app.get('/')
def index():
    return "My name is Gustave, This is my API here"



# if __name__ == '__main__':
#         app.run()


