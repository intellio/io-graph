from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OperatingSystemVersionRange(BaseModel):
	description: Optional[str] = Field(alias="description", default=None,)
	highestVersion: Optional[str] = Field(alias="highestVersion", default=None,)
	lowestVersion: Optional[str] = Field(alias="lowestVersion", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


