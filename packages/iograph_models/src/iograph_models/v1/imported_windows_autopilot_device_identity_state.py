from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ImportedWindowsAutopilotDeviceIdentityState(BaseModel):
	deviceErrorCode: Optional[int] = Field(alias="deviceErrorCode",default=None,)
	deviceErrorName: Optional[str] = Field(alias="deviceErrorName",default=None,)
	deviceImportStatus: Optional[ImportedWindowsAutopilotDeviceIdentityImportStatus | str] = Field(alias="deviceImportStatus",default=None,)
	deviceRegistrationId: Optional[str] = Field(alias="deviceRegistrationId",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .imported_windows_autopilot_device_identity_import_status import ImportedWindowsAutopilotDeviceIdentityImportStatus

