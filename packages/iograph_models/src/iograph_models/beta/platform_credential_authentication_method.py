from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PlatformCredentialAuthenticationMethod(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.platformCredentialAuthenticationMethod"] = Field(alias="@odata.type", default="#microsoft.graph.platformCredentialAuthenticationMethod")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	keyStrength: Optional[AuthenticationMethodKeyStrength | str] = Field(alias="keyStrength", default=None,)
	platform: Optional[AuthenticationMethodPlatform | str] = Field(alias="platform", default=None,)
	device: Optional[Device] = Field(alias="device", default=None,)

from .authentication_method_key_strength import AuthenticationMethodKeyStrength
from .authentication_method_platform import AuthenticationMethodPlatform
from .device import Device

