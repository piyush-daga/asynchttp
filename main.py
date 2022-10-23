from __future__ import annotations
import logging
from typing import List, Dict, Any, Optional, Type
from types import TracebackType

import anyio

import backoff
import httpx

from constants import ALLOWED_HTTP_METHODS, HTTPMethods

logging.getLogger("backoff").addHandler(logging.StreamHandler())
logging.getLogger("backoff").setLevel(logging.INFO)


class AsyncHTTPRequest:
    def __init__(
        self,
        common_headers: Optional[Dict[str, Any]] = None,
        common_params: Optional[Dict[str, Any]] = None,
        max_concurrency: Optional[int] = None,
    ) -> None:
        self.common_headers = common_headers
        self.common_params = common_params
        self.buffer: List[Dict[str, Any]] = list()
        self.max_concurrency = max_concurrency
        self.task_group = anyio.create_task_group()

    async def _request(self, url: str, method: str):
        if method.upper() not in ALLOWED_HTTP_METHODS:
            raise ValueError(f"Specified http method is not valid. Valid list includes: {ALLOWED_HTTP_METHODS}")

        async with httpx.AsyncClient(headers=self.common_headers, params=self.common_params) as client:
            pass

    async def get(self, url: str):
        method = HTTPMethods.get.value
        self.task_group.start_soon(self._request, url, method)

    async def __aenter__(self) -> AsyncHTTPRequest:
        await self.task_group.__aenter__()
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        await self.task_group.__aexit__(exc_type=exc_type, exc_tb=traceback, exc_val=exc_value)
