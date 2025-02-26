from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class WindowsHelloForBusinessAuthenticationMethod(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	keyStrength: Optional[AuthenticationMethodKeyStrength] = Field(default=None,alias="keyStrength",)
	device: Optional[Device] = Field(default=None,alias="device",)

from .authentication_method_key_strength import AuthenticationMethodKeyStrength
from .device import Device

