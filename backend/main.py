from fastapi import FastAPI

app = FastAPI(title='Freelance Lead Finder API')

@app.get('/')
def root():
    return {'status':'ok','app':'Freelance Lead Finder'}
