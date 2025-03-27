from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceConfigurationConflictSummary(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	conflictingDeviceConfigurations: Optional[list[SettingSource]] = Field(alias="conflictingDeviceConfigurations", default=None,)
	contributingSettings: Optional[list[str]] = Field(alias="contributingSettings", default=None,)
	deviceCheckinsImpacted: Optional[int] = Field(alias="deviceCheckinsImpacted", default=None,)

from .setting_source import SettingSource

