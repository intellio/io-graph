from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class LocationConstraint(BaseModel):
	isRequired: Optional[bool] = Field(default=None,alias="isRequired",)
	locations: Optional[list[LocationConstraintItem]] = Field(default=None,alias="locations",)
	suggestLocation: Optional[bool] = Field(default=None,alias="suggestLocation",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .location_constraint_item import LocationConstraintItem

