from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field


class LocalAdminSettings(BaseModel):
	enableGlobalAdmins: Optional[bool] = Field(alias="enableGlobalAdmins", default=None,)
	registeringUsers: Optional[Union[AllDeviceRegistrationMembership, EnumeratedDeviceRegistrationMembership, NoDeviceRegistrationMembership]] = Field(alias="registeringUsers", default=None,discriminator="odata_type", )
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .all_device_registration_membership import AllDeviceRegistrationMembership
from .enumerated_device_registration_membership import EnumeratedDeviceRegistrationMembership
from .no_device_registration_membership import NoDeviceRegistrationMembership
