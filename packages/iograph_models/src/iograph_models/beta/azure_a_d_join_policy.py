from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AzureADJoinPolicy(BaseModel):
	allowedToJoin: SerializeAsAny[Optional[DeviceRegistrationMembership]] = Field(alias="allowedToJoin",default=None,)
	isAdminConfigurable: Optional[bool] = Field(alias="isAdminConfigurable",default=None,)
	localAdmins: Optional[LocalAdminSettings] = Field(alias="localAdmins",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .device_registration_membership import DeviceRegistrationMembership
from .local_admin_settings import LocalAdminSettings

