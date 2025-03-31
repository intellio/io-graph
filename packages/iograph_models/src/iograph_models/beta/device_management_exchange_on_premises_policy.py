from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DeviceManagementExchangeOnPremisesPolicy(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.deviceManagementExchangeOnPremisesPolicy"] = Field(alias="@odata.type",)
	accessRules: Optional[list[DeviceManagementExchangeAccessRule]] = Field(alias="accessRules", default=None,)
	defaultAccessLevel: Optional[DeviceManagementExchangeAccessLevel | str] = Field(alias="defaultAccessLevel", default=None,)
	knownDeviceClasses: Optional[list[DeviceManagementExchangeDeviceClass]] = Field(alias="knownDeviceClasses", default=None,)
	notificationContent: Optional[str] = Field(alias="notificationContent", default=None,)
	conditionalAccessSettings: Optional[OnPremisesConditionalAccessSettings] = Field(alias="conditionalAccessSettings", default=None,)

from .device_management_exchange_access_rule import DeviceManagementExchangeAccessRule
from .device_management_exchange_access_level import DeviceManagementExchangeAccessLevel
from .device_management_exchange_device_class import DeviceManagementExchangeDeviceClass
from .on_premises_conditional_access_settings import OnPremisesConditionalAccessSettings
