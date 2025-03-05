from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CoachmarkLocation(BaseModel):
	length: Optional[int] = Field(default=None,alias="length",)
	offset: Optional[int] = Field(default=None,alias="offset",)
	type: Optional[CoachmarkLocationType] = Field(default=None,alias="type",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .coachmark_location_type import CoachmarkLocationType

