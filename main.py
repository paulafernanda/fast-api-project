import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

import api.models, api.message, api.statistic
from api.database import engine

api.models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(api.message.router, tags=['Message'], prefix='/api/message')
app.include_router(api.statistic.router, tags=['Statistic'], prefix='/api/statistic')

@app.get("/")
def index() -> RedirectResponse:
    return RedirectResponse(url='/docs/')

if __name__ == "__main__":
    uvicorn.run(app, port=8001)