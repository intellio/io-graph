from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class WindowsKioskAzureADGroup(BaseModel):
	odata_type: Literal["#microsoft.graph.windowsKioskAzureADGroup"] = Field(alias="@odata.type", default="#microsoft.graph.windowsKioskAzureADGroup")
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	groupId: Optional[str] = Field(alias="groupId", default=None,)

