from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class HardwareOathTokenAuthenticationMethodDevice(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	hardwareOathDevices: Optional[list[HardwareOathTokenAuthenticationMethodDevice]] = Field(alias="hardwareOathDevices",default=None,)
	assignedTo: SerializeAsAny[Optional[Identity]] = Field(alias="assignedTo",default=None,)
	hashFunction: Optional[HardwareOathTokenHashFunction | str] = Field(alias="hashFunction",default=None,)
	manufacturer: Optional[str] = Field(alias="manufacturer",default=None,)
	model: Optional[str] = Field(alias="model",default=None,)
	secretKey: Optional[str] = Field(alias="secretKey",default=None,)
	serialNumber: Optional[str] = Field(alias="serialNumber",default=None,)
	status: Optional[HardwareOathTokenStatus | str] = Field(alias="status",default=None,)
	timeIntervalInSeconds: Optional[int] = Field(alias="timeIntervalInSeconds",default=None,)
	assignTo: Optional[User] = Field(alias="assignTo",default=None,)

from .identity import Identity
from .hardware_oath_token_hash_function import HardwareOathTokenHashFunction
from .hardware_oath_token_status import HardwareOathTokenStatus
from .user import User

