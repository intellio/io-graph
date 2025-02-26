from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ImportedWindowsAutopilotDeviceIdentity(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	assignedUserPrincipalName: Optional[str] = Field(default=None,alias="assignedUserPrincipalName",)
	groupTag: Optional[str] = Field(default=None,alias="groupTag",)
	hardwareIdentifier: Optional[str] = Field(default=None,alias="hardwareIdentifier",)
	importId: Optional[str] = Field(default=None,alias="importId",)
	productKey: Optional[str] = Field(default=None,alias="productKey",)
	serialNumber: Optional[str] = Field(default=None,alias="serialNumber",)
	state: Optional[ImportedWindowsAutopilotDeviceIdentityState] = Field(default=None,alias="state",)

from .imported_windows_autopilot_device_identity_state import ImportedWindowsAutopilotDeviceIdentityState

