from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IosStoreAppAssignmentSettings(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	isRemovable: Optional[bool] = Field(alias="isRemovable",default=None,)
	uninstallOnDeviceRemoval: Optional[bool] = Field(alias="uninstallOnDeviceRemoval",default=None,)
	vpnConfigurationId: Optional[str] = Field(alias="vpnConfigurationId",default=None,)


