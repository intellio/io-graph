from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ExactMatchSessionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[ExactMatchSession]] = Field(alias="value", default=None,)

from .exact_match_session import ExactMatchSession
