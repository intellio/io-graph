from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AlteredQueryTokenCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[AlteredQueryToken] = Field(alias="value",)

from .altered_query_token import AlteredQueryToken

