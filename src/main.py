import uvicorn
from fastapi import FastAPI
import src.api as api

app = FastAPI()

def main():
    api.RoutersRegistry.init(app)
    uvicorn.run(
        app = app,
        host = '0.0.0.0',
        port = 8000,
    )


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass