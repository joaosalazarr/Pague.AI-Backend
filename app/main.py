from fastapi import FastAPI
from app.api.v1 import auth_router, user_router, company_router

app = FastAPI(title='Pague.AI API')

app.include_router(auth_router.router)
app.include_router(user_router.router)
app.include_router(company_router.router)
