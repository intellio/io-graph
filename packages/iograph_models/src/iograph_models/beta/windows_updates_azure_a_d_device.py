from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import BaseModel, Field


class WindowsUpdatesAzureADDevice(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.windowsUpdates.azureADDevice"] = Field(alias="@odata.type", default="#microsoft.graph.windowsUpdates.azureADDevice")
	enrollment: Optional[WindowsUpdatesUpdateManagementEnrollment] = Field(alias="enrollment", default=None,)
	errors: Optional[list[Annotated[Union[WindowsUpdatesAzureADDeviceRegistrationError],Field(discriminator="odata_type")]]] = Field(alias="errors", default=None,)

from .windows_updates_update_management_enrollment import WindowsUpdatesUpdateManagementEnrollment
from .windows_updates_azure_a_d_device_registration_error import WindowsUpdatesAzureADDeviceRegistrationError
