from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ImportPostRequest(BaseModel):
	importedWindowsAutopilotDeviceIdentities: Optional[list[ImportedWindowsAutopilotDeviceIdentity]] = Field(alias="importedWindowsAutopilotDeviceIdentities",default=None,)

from .imported_windows_autopilot_device_identity import ImportedWindowsAutopilotDeviceIdentity

