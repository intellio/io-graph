from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementIntentCustomizedSetting(BaseModel):
	customizedJson: Optional[str] = Field(alias="customizedJson", default=None,)
	defaultJson: Optional[str] = Field(alias="defaultJson", default=None,)
	definitionId: Optional[str] = Field(alias="definitionId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


