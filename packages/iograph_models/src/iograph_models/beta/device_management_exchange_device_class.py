from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementExchangeDeviceClass(BaseModel):
	name: Optional[str] = Field(alias="name",default=None,)
	type: Optional[DeviceManagementExchangeAccessRuleType | str] = Field(alias="type",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .device_management_exchange_access_rule_type import DeviceManagementExchangeAccessRuleType

