from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class MicrosoftAuthenticatorAuthenticationMethod(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	clientAppName: Optional[MicrosoftAuthenticatorAuthenticationMethodClientAppName | str] = Field(alias="clientAppName",default=None,)
	deviceTag: Optional[str] = Field(alias="deviceTag",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	phoneAppVersion: Optional[str] = Field(alias="phoneAppVersion",default=None,)
	device: Optional[Device] = Field(alias="device",default=None,)

from .microsoft_authenticator_authentication_method_client_app_name import MicrosoftAuthenticatorAuthenticationMethodClientAppName
from .device import Device

