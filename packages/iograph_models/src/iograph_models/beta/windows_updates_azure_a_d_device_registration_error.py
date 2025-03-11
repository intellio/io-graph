from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdatesAzureADDeviceRegistrationError(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	reason: Optional[WindowsUpdatesAzureADDeviceRegistrationErrorReason | str] = Field(alias="reason",default=None,)

from .windows_updates_azure_a_d_device_registration_error_reason import WindowsUpdatesAzureADDeviceRegistrationErrorReason

