from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DeviceConfigurationConflictSummary(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.deviceConfigurationConflictSummary"] = Field(alias="@odata.type", default="#microsoft.graph.deviceConfigurationConflictSummary")
	conflictingDeviceConfigurations: Optional[list[SettingSource]] = Field(alias="conflictingDeviceConfigurations", default=None,)
	contributingSettings: Optional[list[str]] = Field(alias="contributingSettings", default=None,)
	deviceCheckinsImpacted: Optional[int] = Field(alias="deviceCheckinsImpacted", default=None,)

from .setting_source import SettingSource
