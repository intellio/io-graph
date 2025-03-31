from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DeviceManagementConfigurationSettingValueTemplateReference(BaseModel):
	settingValueTemplateId: Optional[str] = Field(alias="settingValueTemplateId", default=None,)
	useTemplateDefault: Optional[bool] = Field(alias="useTemplateDefault", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

