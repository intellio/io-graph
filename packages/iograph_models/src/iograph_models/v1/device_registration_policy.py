from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DeviceRegistrationPolicy(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.deviceRegistrationPolicy"] = Field(alias="@odata.type", default="#microsoft.graph.deviceRegistrationPolicy")
	azureADJoin: Optional[AzureADJoinPolicy] = Field(alias="azureADJoin", default=None,)
	azureADRegistration: Optional[AzureADRegistrationPolicy] = Field(alias="azureADRegistration", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	localAdminPassword: Optional[LocalAdminPasswordSettings] = Field(alias="localAdminPassword", default=None,)
	multiFactorAuthConfiguration: Optional[MultiFactorAuthConfiguration | str] = Field(alias="multiFactorAuthConfiguration", default=None,)
	userDeviceQuota: Optional[int] = Field(alias="userDeviceQuota", default=None,)

from .azure_a_d_join_policy import AzureADJoinPolicy
from .azure_a_d_registration_policy import AzureADRegistrationPolicy
from .local_admin_password_settings import LocalAdminPasswordSettings
from .multi_factor_auth_configuration import MultiFactorAuthConfiguration
