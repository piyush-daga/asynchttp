from __future__ import annotations
import logging
from typing import List , Dict, Any, Optional, Type
from types import TracebackType

import anyio

import backoff
import httpx

logging.getLogger('backoff').addHandler(logging.StreamHandler())
logging.getLogger('backoff').setLevel(logging.INFO)


class AsyncHTTPRequest:
    def __init__(
        self, common_headers: Optional[Dict[str, Any]] = None, common_params: Optional[Dict[str, Any]] = None, max_concurrency: Optional[int] = None
    ) -> None:
        self.common_headers = common_headers
        self.common_params = common_params
        self.buffer: List[Dict[str, Any]] = list()
        self.max_concurrency = max_concurrency
    
    def get(self, url: str):
        print(f'Doing something with {url}')
    
    def __enter__(self) -> AsyncHTTPRequest:
        print('Entered here')
        return self

    def __exit__(
        self, exc_type: Optional[Type[BaseException]], exc_value: Optional[BaseException], traceback: Optional[TracebackType]
    ) -> None:
        print('Done with the work')
