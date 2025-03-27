from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdateActiveHoursInstall(BaseModel):
	odata_type: Literal["#microsoft.graph.windowsUpdateActiveHoursInstall"] = Field(alias="@odata.type", default="#microsoft.graph.windowsUpdateActiveHoursInstall")
	activeHoursEnd: Optional[str] = Field(alias="activeHoursEnd", default=None,)
	activeHoursStart: Optional[str] = Field(alias="activeHoursStart", default=None,)


