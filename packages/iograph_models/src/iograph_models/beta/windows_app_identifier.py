from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class WindowsAppIdentifier(BaseModel):
	odata_type: Literal["#microsoft.graph.windowsAppIdentifier"] = Field(alias="@odata.type", default="#microsoft.graph.windowsAppIdentifier")
	windowsAppId: Optional[str] = Field(alias="windowsAppId", default=None,)

