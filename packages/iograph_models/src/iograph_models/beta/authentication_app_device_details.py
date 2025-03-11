from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AuthenticationAppDeviceDetails(BaseModel):
	appVersion: Optional[str] = Field(alias="appVersion",default=None,)
	clientApp: Optional[str] = Field(alias="clientApp",default=None,)
	deviceId: Optional[str] = Field(alias="deviceId",default=None,)
	operatingSystem: Optional[str] = Field(alias="operatingSystem",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


