from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class LocationConstraint(BaseModel):
	isRequired: Optional[bool] = Field(alias="isRequired",default=None,)
	locations: Optional[list[LocationConstraintItem]] = Field(alias="locations",default=None,)
	suggestLocation: Optional[bool] = Field(alias="suggestLocation",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .location_constraint_item import LocationConstraintItem

