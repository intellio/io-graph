from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdatesAzureADDeviceRegistrationError(BaseModel):
	odata_type: Literal["#microsoft.graph.windowsUpdates.azureADDeviceRegistrationError"] = Field(alias="@odata.type", default="#microsoft.graph.windowsUpdates.azureADDeviceRegistrationError")
	reason: Optional[WindowsUpdatesAzureADDeviceRegistrationErrorReason | str] = Field(alias="reason", default=None,)

from .windows_updates_azure_a_d_device_registration_error_reason import WindowsUpdatesAzureADDeviceRegistrationErrorReason

