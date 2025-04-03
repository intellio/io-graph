from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class WindowsManagementAppHealthSummary(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.windowsManagementAppHealthSummary"] = Field(alias="@odata.type", default="#microsoft.graph.windowsManagementAppHealthSummary")
	healthyDeviceCount: Optional[int] = Field(alias="healthyDeviceCount", default=None,)
	unhealthyDeviceCount: Optional[int] = Field(alias="unhealthyDeviceCount", default=None,)
	unknownDeviceCount: Optional[int] = Field(alias="unknownDeviceCount", default=None,)

