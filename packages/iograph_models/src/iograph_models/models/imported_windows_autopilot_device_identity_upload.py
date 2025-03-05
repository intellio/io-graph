from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ImportedWindowsAutopilotDeviceIdentityUpload(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTimeUtc: Optional[datetime] = Field(default=None,alias="createdDateTimeUtc",)
	status: Optional[ImportedWindowsAutopilotDeviceIdentityUploadStatus] = Field(default=None,alias="status",)
	deviceIdentities: Optional[list[ImportedWindowsAutopilotDeviceIdentity]] = Field(default=None,alias="deviceIdentities",)

from .imported_windows_autopilot_device_identity_upload_status import ImportedWindowsAutopilotDeviceIdentityUploadStatus
from .imported_windows_autopilot_device_identity import ImportedWindowsAutopilotDeviceIdentity

