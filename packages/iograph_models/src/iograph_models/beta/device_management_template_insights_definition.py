from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DeviceManagementTemplateInsightsDefinition(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.deviceManagementTemplateInsightsDefinition"] = Field(alias="@odata.type",)
	settingInsights: Optional[list[DeviceManagementSettingInsightsDefinition]] = Field(alias="settingInsights", default=None,)

from .device_management_setting_insights_definition import DeviceManagementSettingInsightsDefinition
