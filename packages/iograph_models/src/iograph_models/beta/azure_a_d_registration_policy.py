from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AzureADRegistrationPolicy(BaseModel):
	allowedToRegister: SerializeAsAny[Optional[DeviceRegistrationMembership]] = Field(alias="allowedToRegister",default=None,)
	isAdminConfigurable: Optional[bool] = Field(alias="isAdminConfigurable",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .device_registration_membership import DeviceRegistrationMembership

