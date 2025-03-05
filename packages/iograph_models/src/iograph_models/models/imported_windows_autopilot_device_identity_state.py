from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ImportedWindowsAutopilotDeviceIdentityState(BaseModel):
	deviceErrorCode: Optional[int] = Field(default=None,alias="deviceErrorCode",)
	deviceErrorName: Optional[str] = Field(default=None,alias="deviceErrorName",)
	deviceImportStatus: Optional[ImportedWindowsAutopilotDeviceIdentityImportStatus] = Field(default=None,alias="deviceImportStatus",)
	deviceRegistrationId: Optional[str] = Field(default=None,alias="deviceRegistrationId",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .imported_windows_autopilot_device_identity_import_status import ImportedWindowsAutopilotDeviceIdentityImportStatus

