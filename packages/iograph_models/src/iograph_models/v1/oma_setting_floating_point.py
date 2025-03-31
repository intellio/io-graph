from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class OmaSettingFloatingPoint(BaseModel):
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	omaUri: Optional[str] = Field(alias="omaUri", default=None,)
	odata_type: Literal["#microsoft.graph.omaSettingFloatingPoint"] = Field(alias="@odata.type", default="#microsoft.graph.omaSettingFloatingPoint")
	value: float | str | ReferenceNumeric

from .reference_numeric import ReferenceNumeric
