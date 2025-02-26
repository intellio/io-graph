from __future__ import annotations
from enum import Enum


class ImportedWindowsAutopilotDeviceIdentityUploadStatus(Enum):
	noUpload = "noUpload"
	pending = "pending"
	complete = "complete"
	error = "error"

