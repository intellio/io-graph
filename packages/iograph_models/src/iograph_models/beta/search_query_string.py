from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SearchQueryString(BaseModel):
	query: Optional[str] = Field(alias="query", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


