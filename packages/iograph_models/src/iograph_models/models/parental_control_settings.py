from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ParentalControlSettings(BaseModel):
	countriesBlockedForMinors: list[Optional[str]] = Field(alias="countriesBlockedForMinors",)
	legalAgeGroupRule: Optional[str] = Field(default=None,alias="legalAgeGroupRule",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


