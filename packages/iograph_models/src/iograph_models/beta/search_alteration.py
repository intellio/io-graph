from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SearchAlteration(BaseModel):
	alteredHighlightedQueryString: Optional[str] = Field(alias="alteredHighlightedQueryString", default=None,)
	alteredQueryString: Optional[str] = Field(alias="alteredQueryString", default=None,)
	alteredQueryTokens: Optional[list[AlteredQueryToken]] = Field(alias="alteredQueryTokens", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .altered_query_token import AlteredQueryToken
