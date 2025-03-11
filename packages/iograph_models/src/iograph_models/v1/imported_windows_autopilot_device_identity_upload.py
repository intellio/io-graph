from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ImportedWindowsAutopilotDeviceIdentityUpload(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTimeUtc: Optional[datetime] = Field(alias="createdDateTimeUtc",default=None,)
	status: Optional[ImportedWindowsAutopilotDeviceIdentityUploadStatus | str] = Field(alias="status",default=None,)
	deviceIdentities: Optional[list[ImportedWindowsAutopilotDeviceIdentity]] = Field(alias="deviceIdentities",default=None,)

from .imported_windows_autopilot_device_identity_upload_status import ImportedWindowsAutopilotDeviceIdentityUploadStatus
from .imported_windows_autopilot_device_identity import ImportedWindowsAutopilotDeviceIdentity

