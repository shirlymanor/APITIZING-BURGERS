"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from ._hooks import SDKHooks
from .httpclient import AsyncHttpClient, HttpClient
from .utils import Logger, RetryConfig, remove_suffix
from burger_sdk.types import OptionalNullable, UNSET
from dataclasses import dataclass
from pydantic import Field
from typing import Dict, Optional, Tuple


SERVERS = [
    "http://127.0.0.1:8000/",
    # Local server
]
"""Contains the list of servers available to the SDK"""


@dataclass
class SDKConfiguration:
    client: HttpClient
    async_client: AsyncHttpClient
    debug_logger: Logger
    server_url: Optional[str] = ""
    server_idx: Optional[int] = 0
    language: str = "python"
    openapi_doc_version: str = "0.1.0"
    sdk_version: str = "0.1.1"
    gen_version: str = "2.457.9"
    user_agent: str = "speakeasy-sdk/python 0.1.1 2.457.9 0.1.0 burger-sdk"
    retry_config: OptionalNullable[RetryConfig] = Field(default_factory=lambda: UNSET)
    timeout_ms: Optional[int] = None

    def __post_init__(self):
        self._hooks = SDKHooks()

    def get_server_details(self) -> Tuple[str, Dict[str, str]]:
        if self.server_url is not None and self.server_url:
            return remove_suffix(self.server_url, "/"), {}
        if self.server_idx is None:
            self.server_idx = 0

        return SERVERS[self.server_idx], {}

    def get_hooks(self) -> SDKHooks:
        return self._hooks
