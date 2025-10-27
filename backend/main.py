from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import products, suppliers

app = FastAPI(title="MVP1688")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(products.router)
app.include_router(suppliers.router)

@app.get("/")
def root():
    return {"message": "MVP1688 backend работает"}