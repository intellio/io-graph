from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class QueryPostRequest(BaseModel):
	requests: Optional[list[SearchRequest]] = Field(default=None,alias="requests",)

from .search_request import SearchRequest

