from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class WindowsInformationProtectionNetworkLearningSummary(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.windowsInformationProtectionNetworkLearningSummary"] = Field(alias="@odata.type",)
	deviceCount: Optional[int] = Field(alias="deviceCount", default=None,)
	url: Optional[str] = Field(alias="url", default=None,)

