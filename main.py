from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import uvicorn

app = FastAPI()

origins = ["https://improved-waddle-q7v66j6qr99rf9w56-5173.app.github.dev", "http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Ajusta el puerto según tu React
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"mensaje": "Hola desde FastAPI"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

