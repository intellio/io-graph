from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class HardwareOathAuthenticationMethod(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	device: Optional[HardwareOathTokenAuthenticationMethodDevice] = Field(alias="device",default=None,)

from .hardware_oath_token_authentication_method_device import HardwareOathTokenAuthenticationMethodDevice

