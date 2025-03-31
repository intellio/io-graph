from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class WindowsAppXAppAssignmentSettings(BaseModel):
	odata_type: Literal["#microsoft.graph.windowsAppXAppAssignmentSettings"] = Field(alias="@odata.type", default="#microsoft.graph.windowsAppXAppAssignmentSettings")
	useDeviceContext: Optional[bool] = Field(alias="useDeviceContext", default=None,)

