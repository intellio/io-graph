from __future__ import annotations
from pydantic import BaseModel, Field


class QueryPostRequest(BaseModel):
	requests: list[SearchRequest] = Field(alias="requests",)

from .search_request import SearchRequest

