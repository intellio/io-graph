from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class OmaSettingString(BaseModel):
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	omaUri: Optional[str] = Field(alias="omaUri", default=None,)
	odata_type: Literal["#microsoft.graph.omaSettingString"] = Field(alias="@odata.type", default="#microsoft.graph.omaSettingString")
	value: Optional[str] = Field(alias="value", default=None,)

