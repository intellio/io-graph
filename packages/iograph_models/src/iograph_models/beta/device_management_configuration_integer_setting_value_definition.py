from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementConfigurationIntegerSettingValueDefinition(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	maximumValue: Optional[int] = Field(alias="maximumValue",default=None,)
	minimumValue: Optional[int] = Field(alias="minimumValue",default=None,)


