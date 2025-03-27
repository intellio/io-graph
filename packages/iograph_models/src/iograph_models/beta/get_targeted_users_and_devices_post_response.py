from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Get_targeted_users_and_devicesPostResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[DeviceConfigurationTargetedUserAndDevice]] = Field(alias="value", default=None,)

from .device_configuration_targeted_user_and_device import DeviceConfigurationTargetedUserAndDevice

