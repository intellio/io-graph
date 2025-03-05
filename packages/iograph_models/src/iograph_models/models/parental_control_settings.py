from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ParentalControlSettings(BaseModel):
	countriesBlockedForMinors: Optional[list[str]] = Field(alias="countriesBlockedForMinors",default=None,)
	legalAgeGroupRule: Optional[str] = Field(alias="legalAgeGroupRule",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


