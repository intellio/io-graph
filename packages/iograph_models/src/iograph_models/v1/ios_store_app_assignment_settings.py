from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class IosStoreAppAssignmentSettings(BaseModel):
	odata_type: Literal["#microsoft.graph.iosStoreAppAssignmentSettings"] = Field(alias="@odata.type", default="#microsoft.graph.iosStoreAppAssignmentSettings")
	isRemovable: Optional[bool] = Field(alias="isRemovable", default=None,)
	uninstallOnDeviceRemoval: Optional[bool] = Field(alias="uninstallOnDeviceRemoval", default=None,)
	vpnConfigurationId: Optional[str] = Field(alias="vpnConfigurationId", default=None,)


