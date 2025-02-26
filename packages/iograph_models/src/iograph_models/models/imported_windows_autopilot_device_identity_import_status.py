from __future__ import annotations
from enum import Enum


class ImportedWindowsAutopilotDeviceIdentityImportStatus(Enum):
	unknown = "unknown"
	pending = "pending"
	partial = "partial"
	complete = "complete"
	error = "error"

