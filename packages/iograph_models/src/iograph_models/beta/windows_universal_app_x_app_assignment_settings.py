from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUniversalAppXAppAssignmentSettings(BaseModel):
	odata_type: Literal["#microsoft.graph.windowsUniversalAppXAppAssignmentSettings"] = Field(alias="@odata.type", default="#microsoft.graph.windowsUniversalAppXAppAssignmentSettings")
	useDeviceContext: Optional[bool] = Field(alias="useDeviceContext", default=None,)


