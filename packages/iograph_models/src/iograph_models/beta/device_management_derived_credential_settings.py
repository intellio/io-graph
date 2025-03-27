from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementDerivedCredentialSettings(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	helpUrl: Optional[str] = Field(alias="helpUrl", default=None,)
	issuer: Optional[DeviceManagementDerivedCredentialIssuer | str] = Field(alias="issuer", default=None,)
	notificationType: Optional[DeviceManagementDerivedCredentialNotificationType | str] = Field(alias="notificationType", default=None,)
	renewalThresholdPercentage: Optional[int] = Field(alias="renewalThresholdPercentage", default=None,)

from .device_management_derived_credential_issuer import DeviceManagementDerivedCredentialIssuer
from .device_management_derived_credential_notification_type import DeviceManagementDerivedCredentialNotificationType

