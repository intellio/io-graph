from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class MacOsLobAppAssignmentSettings(BaseModel):
	odata_type: Literal["#microsoft.graph.macOsLobAppAssignmentSettings"] = Field(alias="@odata.type", default="#microsoft.graph.macOsLobAppAssignmentSettings")
	uninstallOnDeviceRemoval: Optional[bool] = Field(alias="uninstallOnDeviceRemoval", default=None,)


