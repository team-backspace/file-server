from fastapi import FastAPI
import uvicorn

from router.file import router as file_router

app = FastAPI(
    title="Spacebook FileServer",
    description="Spacebook FileServer, fastapi",
    version="0.1",
    docs_url="/development-docs",
    redoc_url="/development-redoc",
)
app.include_router(file_router)


@app.get("/")
async def main():
    return {"hello" : "world"}

uvicorn.run(app)