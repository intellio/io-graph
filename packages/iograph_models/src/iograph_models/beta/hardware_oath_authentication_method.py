from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class HardwareOathAuthenticationMethod(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.hardwareOathAuthenticationMethod"] = Field(alias="@odata.type", default="#microsoft.graph.hardwareOathAuthenticationMethod")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	device: Optional[HardwareOathTokenAuthenticationMethodDevice] = Field(alias="device", default=None,)

from .hardware_oath_token_authentication_method_device import HardwareOathTokenAuthenticationMethodDevice
