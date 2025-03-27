from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceDetail(BaseModel):
	browser: Optional[str] = Field(alias="browser", default=None,)
	deviceId: Optional[str] = Field(alias="deviceId", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	isCompliant: Optional[bool] = Field(alias="isCompliant", default=None,)
	isManaged: Optional[bool] = Field(alias="isManaged", default=None,)
	operatingSystem: Optional[str] = Field(alias="operatingSystem", default=None,)
	trustType: Optional[str] = Field(alias="trustType", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


