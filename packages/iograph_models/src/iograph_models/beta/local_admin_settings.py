from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class LocalAdminSettings(BaseModel):
	enableGlobalAdmins: Optional[bool] = Field(alias="enableGlobalAdmins",default=None,)
	registeringUsers: SerializeAsAny[Optional[DeviceRegistrationMembership]] = Field(alias="registeringUsers",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .device_registration_membership import DeviceRegistrationMembership

