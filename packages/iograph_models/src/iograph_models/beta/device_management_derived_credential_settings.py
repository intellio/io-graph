from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DeviceManagementDerivedCredentialSettings(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.deviceManagementDerivedCredentialSettings"] = Field(alias="@odata.type", default="#microsoft.graph.deviceManagementDerivedCredentialSettings")
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	helpUrl: Optional[str] = Field(alias="helpUrl", default=None,)
	issuer: Optional[DeviceManagementDerivedCredentialIssuer | str] = Field(alias="issuer", default=None,)
	notificationType: Optional[DeviceManagementDerivedCredentialNotificationType | str] = Field(alias="notificationType", default=None,)
	renewalThresholdPercentage: Optional[int] = Field(alias="renewalThresholdPercentage", default=None,)

from .device_management_derived_credential_issuer import DeviceManagementDerivedCredentialIssuer
from .device_management_derived_credential_notification_type import DeviceManagementDerivedCredentialNotificationType
