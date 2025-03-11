from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementConfigurationIntegerSettingValueDefinitionTemplate(BaseModel):
	maxValue: Optional[int] = Field(alias="maxValue",default=None,)
	minValue: Optional[int] = Field(alias="minValue",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


