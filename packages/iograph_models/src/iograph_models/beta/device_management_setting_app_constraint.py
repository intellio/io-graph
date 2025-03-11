from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementSettingAppConstraint(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	supportedTypes: Optional[list[str]] = Field(alias="supportedTypes",default=None,)


