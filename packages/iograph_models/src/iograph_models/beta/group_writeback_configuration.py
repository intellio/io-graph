from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class GroupWritebackConfiguration(BaseModel):
	isEnabled: Optional[bool] = Field(alias="isEnabled", default=None,)
	odata_type: Literal["#microsoft.graph.groupWritebackConfiguration"] = Field(alias="@odata.type", default="#microsoft.graph.groupWritebackConfiguration")
	onPremisesGroupType: Optional[str] = Field(alias="onPremisesGroupType", default=None,)

