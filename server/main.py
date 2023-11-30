
from fastapi import FastAPI
from database import connect

app = FastAPI()
conn = connect()
cursor = conn.cursor()


