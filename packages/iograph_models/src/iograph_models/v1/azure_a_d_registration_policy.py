from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field


class AzureADRegistrationPolicy(BaseModel):
	allowedToRegister: Optional[Union[AllDeviceRegistrationMembership, EnumeratedDeviceRegistrationMembership, NoDeviceRegistrationMembership]] = Field(alias="allowedToRegister", default=None,discriminator="odata_type", )
	isAdminConfigurable: Optional[bool] = Field(alias="isAdminConfigurable", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .all_device_registration_membership import AllDeviceRegistrationMembership
from .enumerated_device_registration_membership import EnumeratedDeviceRegistrationMembership
from .no_device_registration_membership import NoDeviceRegistrationMembership
