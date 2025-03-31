from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DeviceManagementConfigurationReferredSettingInformation(BaseModel):
	settingDefinitionId: Optional[str] = Field(alias="settingDefinitionId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

