from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceDetail(BaseModel):
	browser: Optional[str] = Field(default=None,alias="browser",)
	deviceId: Optional[str] = Field(default=None,alias="deviceId",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	isCompliant: Optional[bool] = Field(default=None,alias="isCompliant",)
	isManaged: Optional[bool] = Field(default=None,alias="isManaged",)
	operatingSystem: Optional[str] = Field(default=None,alias="operatingSystem",)
	trustType: Optional[str] = Field(default=None,alias="trustType",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


