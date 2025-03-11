from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementConfigurationStringSettingValueConstantDefaultTemplate(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	constantValue: Optional[str] = Field(alias="constantValue",default=None,)


