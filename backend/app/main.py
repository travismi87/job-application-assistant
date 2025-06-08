from contextlib import asynccontextmanager

from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize resources here if needed
    yield
    # Cleanup resources here if needed
    print("Shutting down the application...")


app = FastAPI(
    title="Job Application Assistant API",
    description="An API to assist with job applications, including resume parsing and job matching.",
    version="1.0.0",
    lifespan=lifespan,
)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Job Application Assistant API!"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )
