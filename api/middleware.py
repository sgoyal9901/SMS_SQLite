from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import time

def register_middleware(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:3000", "http://localhost:8000"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.middleware("http")
    async def add_process_time_header(request: Request, call_next):
        start_time = time.perf_counter()
        response = await call_next(request)
        process_time = time.perf_counter() - start_time
        print(f'''
Request URL: {request.url.path}
Method: {request.method}
Status Code: {response.status_code}
Process Time: {process_time:.4f}sec
        ''')
        return response