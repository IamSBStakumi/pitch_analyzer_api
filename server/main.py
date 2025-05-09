from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from handlers import analyze_pitch as ap

server = FastAPI()

origins = [
    "http://localhost:3000",
]

server.add_middleware(
    CORSMiddleware, 
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["get"],
    allow_headers=["*"]
)

@server.get("/")
async def root():
    return {"message": "Hello World"}

server.include_router(
    ap.router,
)

@server.exception_handler(RequestValidationError)
async def handler(request: Request, exc: RequestValidationError):
    print(exc)
    return JSONResponse(content={}, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(server, host="0.0.0.0", port=8080)
