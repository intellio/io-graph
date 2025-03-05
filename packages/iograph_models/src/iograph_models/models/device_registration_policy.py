from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceRegistrationPolicy(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	azureADJoin: Optional[AzureADJoinPolicy] = Field(default=None,alias="azureADJoin",)
	azureADRegistration: Optional[AzureADRegistrationPolicy] = Field(default=None,alias="azureADRegistration",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	localAdminPassword: Optional[LocalAdminPasswordSettings] = Field(default=None,alias="localAdminPassword",)
	multiFactorAuthConfiguration: Optional[MultiFactorAuthConfiguration] = Field(default=None,alias="multiFactorAuthConfiguration",)
	userDeviceQuota: Optional[int] = Field(default=None,alias="userDeviceQuota",)

from .azure_a_d_join_policy import AzureADJoinPolicy
from .azure_a_d_registration_policy import AzureADRegistrationPolicy
from .local_admin_password_settings import LocalAdminPasswordSettings
from .multi_factor_auth_configuration import MultiFactorAuthConfiguration

