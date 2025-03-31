from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class IosLobAppAssignmentSettings(BaseModel):
	odata_type: Literal["#microsoft.graph.iosLobAppAssignmentSettings"] = Field(alias="@odata.type", default="#microsoft.graph.iosLobAppAssignmentSettings")
	isRemovable: Optional[bool] = Field(alias="isRemovable", default=None,)
	uninstallOnDeviceRemoval: Optional[bool] = Field(alias="uninstallOnDeviceRemoval", default=None,)
	vpnConfigurationId: Optional[str] = Field(alias="vpnConfigurationId", default=None,)

