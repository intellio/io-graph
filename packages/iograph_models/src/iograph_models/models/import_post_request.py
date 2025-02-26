from __future__ import annotations
from pydantic import BaseModel, Field


class ImportPostRequest(BaseModel):
	importedWindowsAutopilotDeviceIdentities: list[ImportedWindowsAutopilotDeviceIdentity] = Field(alias="importedWindowsAutopilotDeviceIdentities",)

from .imported_windows_autopilot_device_identity import ImportedWindowsAutopilotDeviceIdentity

