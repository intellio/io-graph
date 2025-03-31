from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TeamsAppCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[TeamsApp]] = Field(alias="value", default=None,)

from .teams_app import TeamsApp
