from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class MicrosoftAuthenticatorAuthenticationMethod(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	deviceTag: Optional[str] = Field(default=None,alias="deviceTag",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	phoneAppVersion: Optional[str] = Field(default=None,alias="phoneAppVersion",)
	device: Optional[Device] = Field(default=None,alias="device",)

from .device import Device

