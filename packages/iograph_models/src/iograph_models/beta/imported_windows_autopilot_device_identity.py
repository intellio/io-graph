from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ImportedWindowsAutopilotDeviceIdentity(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	assignedUserPrincipalName: Optional[str] = Field(alias="assignedUserPrincipalName", default=None,)
	groupTag: Optional[str] = Field(alias="groupTag", default=None,)
	hardwareIdentifier: Optional[str] = Field(alias="hardwareIdentifier", default=None,)
	importId: Optional[str] = Field(alias="importId", default=None,)
	productKey: Optional[str] = Field(alias="productKey", default=None,)
	serialNumber: Optional[str] = Field(alias="serialNumber", default=None,)
	state: Optional[ImportedWindowsAutopilotDeviceIdentityState] = Field(alias="state", default=None,)

from .imported_windows_autopilot_device_identity_state import ImportedWindowsAutopilotDeviceIdentityState

