from fastapi import FastAPI
from routes.user import user 
app = FastAPI()
app.include_router(user)
