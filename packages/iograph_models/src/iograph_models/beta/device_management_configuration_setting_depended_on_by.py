from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementConfigurationSettingDependedOnBy(BaseModel):
	dependedOnBy: Optional[str] = Field(alias="dependedOnBy", default=None,)
	required: Optional[bool] = Field(alias="required", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


