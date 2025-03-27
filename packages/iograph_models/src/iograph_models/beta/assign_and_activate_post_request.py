from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Assign_and_activatePostRequest(BaseModel):
	verificationCode: Optional[str] = Field(alias="verificationCode", default=None,)
	device: Optional[HardwareOathTokenAuthenticationMethodDevice] = Field(alias="device", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)

from .hardware_oath_token_authentication_method_device import HardwareOathTokenAuthenticationMethodDevice

