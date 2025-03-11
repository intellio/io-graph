from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementTemplateInsightsDefinition(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	settingInsights: Optional[list[DeviceManagementSettingInsightsDefinition]] = Field(alias="settingInsights",default=None,)

from .device_management_setting_insights_definition import DeviceManagementSettingInsightsDefinition

