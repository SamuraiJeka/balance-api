from routes.endpoints import router
from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html


app = FastAPI()

app.include_router(router)


@app.get("/test")
async def test(a: int, b: int) -> dict:
    return {"result": a + b}


@app.get("/docs")
def read_docs():
    return get_swagger_ui_html(openapi_url="/openapi.json")
