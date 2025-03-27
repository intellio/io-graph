from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PayloadCoachmark(BaseModel):
	coachmarkLocation: Optional[CoachmarkLocation] = Field(alias="coachmarkLocation", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	indicator: Optional[str] = Field(alias="indicator", default=None,)
	isValid: Optional[bool] = Field(alias="isValid", default=None,)
	language: Optional[str] = Field(alias="language", default=None,)
	order: Optional[str] = Field(alias="order", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .coachmark_location import CoachmarkLocation

