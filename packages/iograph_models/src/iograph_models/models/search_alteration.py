from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SearchAlteration(BaseModel):
	alteredHighlightedQueryString: Optional[str] = Field(default=None,alias="alteredHighlightedQueryString",)
	alteredQueryString: Optional[str] = Field(default=None,alias="alteredQueryString",)
	alteredQueryTokens: Optional[list[AlteredQueryToken]] = Field(default=None,alias="alteredQueryTokens",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .altered_query_token import AlteredQueryToken

