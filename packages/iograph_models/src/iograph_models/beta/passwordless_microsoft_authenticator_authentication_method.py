from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PasswordlessMicrosoftAuthenticatorAuthenticationMethod(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	creationDateTime: Optional[datetime] = Field(alias="creationDateTime",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	device: Optional[Device] = Field(alias="device",default=None,)

from .device import Device

