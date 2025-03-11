from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementSettingProfileConstraint(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	source: Optional[str] = Field(alias="source",default=None,)
	types: Optional[list[str]] = Field(alias="types",default=None,)


