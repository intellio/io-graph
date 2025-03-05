from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PayloadCoachmark(BaseModel):
	coachmarkLocation: Optional[CoachmarkLocation] = Field(default=None,alias="coachmarkLocation",)
	description: Optional[str] = Field(default=None,alias="description",)
	indicator: Optional[str] = Field(default=None,alias="indicator",)
	isValid: Optional[bool] = Field(default=None,alias="isValid",)
	language: Optional[str] = Field(default=None,alias="language",)
	order: Optional[str] = Field(default=None,alias="order",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .coachmark_location import CoachmarkLocation

