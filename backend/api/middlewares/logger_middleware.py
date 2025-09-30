from collections.abc import Callable
from typing import Any
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
import time
from loguru import logger

class LoggerMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: Callable[[Request], Any]
    ) -> Response:
        """
        Logs all incoming and outgoing request, response pairs. This method logs the request params,
        datetime of request, duration of execution. Logs should be printed using the custom logging module provided.
        Logs should be printed so that they are easily readable and understandable.

        :param request: Request received to this middleware from client (it is supplied by FastAPI)
        :param call_next: Endpoint or next middleware to be called (if any, this is the next middleware in the chain of middlewares, it is supplied by FastAPI)
        :return: Response from endpoint
        """
        
        start_time = time.time()
        logger.info(
            f"Incoming request: {request.method} {request.url.path} | "
            f"Query params: {dict(request.query_params)} | "
            f"Client: {request.client.host if request.client else 'unknown'}"
        )
        response = await call_next(request)
        duration = time.time() - start_time
        logger.info(
            f"Outgoing response: {request.method} {request.url.path} | "
            f"Status: {response.status_code} | "
            f"Duration: {duration:.4f}s"
        )
        return response
        # TODO:(Member) Finish implementing this method

