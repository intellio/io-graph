from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class LocationConstraint(BaseModel):
	isRequired: Optional[bool] = Field(default=None,alias="isRequired",)
	locations: list[LocationConstraintItem] = Field(alias="locations",)
	suggestLocation: Optional[bool] = Field(default=None,alias="suggestLocation",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .location_constraint_item import LocationConstraintItem

