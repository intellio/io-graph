from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AzureADJoinPolicy(BaseModel):
	allowedToJoin: SerializeAsAny[Optional[DeviceRegistrationMembership]] = Field(default=None,alias="allowedToJoin",)
	isAdminConfigurable: Optional[bool] = Field(default=None,alias="isAdminConfigurable",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .device_registration_membership import DeviceRegistrationMembership

