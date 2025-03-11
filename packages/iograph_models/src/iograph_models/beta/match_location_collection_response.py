from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MatchLocationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[MatchLocation]] = Field(alias="value",default=None,)

from .match_location import MatchLocation

