from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementConfigurationDependentOn(BaseModel):
	dependentOn: Optional[str] = Field(alias="dependentOn",default=None,)
	parentSettingId: Optional[str] = Field(alias="parentSettingId",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


