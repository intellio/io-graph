from __future__ import annotations
from enum import StrEnum


class ImportedWindowsAutopilotDeviceIdentityUploadStatus(StrEnum):
	noUpload = "noUpload"
	pending = "pending"
	complete = "complete"
	error = "error"

