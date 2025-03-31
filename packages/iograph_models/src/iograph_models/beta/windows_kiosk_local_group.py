from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class WindowsKioskLocalGroup(BaseModel):
	odata_type: Literal["#microsoft.graph.windowsKioskLocalGroup"] = Field(alias="@odata.type", default="#microsoft.graph.windowsKioskLocalGroup")
	groupName: Optional[str] = Field(alias="groupName", default=None,)

