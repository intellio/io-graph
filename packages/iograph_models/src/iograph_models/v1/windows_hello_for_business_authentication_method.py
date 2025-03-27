from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsHelloForBusinessAuthenticationMethod(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.windowsHelloForBusinessAuthenticationMethod"] = Field(alias="@odata.type", default="#microsoft.graph.windowsHelloForBusinessAuthenticationMethod")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	keyStrength: Optional[AuthenticationMethodKeyStrength | str] = Field(alias="keyStrength", default=None,)
	device: Optional[Device] = Field(alias="device", default=None,)

from .authentication_method_key_strength import AuthenticationMethodKeyStrength
from .device import Device

