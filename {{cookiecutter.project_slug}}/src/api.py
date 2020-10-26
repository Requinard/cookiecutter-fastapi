"""
Sets up a FastAPI application and includes all sub-routers
"""
import time

import fastapi
from fastapi import Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

from utilities.settings import settings

api = fastapi.FastAPI(title=f'{{ cookiecutter.project_name }} - {settings.stage}')


@api.get("/", include_in_schema=False)
def redirect_to_docs():
    """
    Automatically redirect users to docs when entering the application
    """
    return RedirectResponse('/docs')


@api.middleware('http')
async def add_extra_headers(request: Request, call_next):
    """
    FastAPI middleware that adds some security and timing headers
    """
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'

    if not settings.is_local:
        response.headers["Content-Security-Policy"] = "upgrade-insecure"

    return response


api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
