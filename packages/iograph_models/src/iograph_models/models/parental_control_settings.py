from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ParentalControlSettings(BaseModel):
	countriesBlockedForMinors: Optional[list[str]] = Field(default=None,alias="countriesBlockedForMinors",)
	legalAgeGroupRule: Optional[str] = Field(default=None,alias="legalAgeGroupRule",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


