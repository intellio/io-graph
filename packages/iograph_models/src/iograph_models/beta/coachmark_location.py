from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CoachmarkLocation(BaseModel):
	length: Optional[int] = Field(alias="length", default=None,)
	offset: Optional[int] = Field(alias="offset", default=None,)
	type: Optional[CoachmarkLocationType | str] = Field(alias="type", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .coachmark_location_type import CoachmarkLocationType
