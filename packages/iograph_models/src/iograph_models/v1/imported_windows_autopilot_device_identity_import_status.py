from __future__ import annotations
from enum import StrEnum


class ImportedWindowsAutopilotDeviceIdentityImportStatus(StrEnum):
	unknown = "unknown"
	pending = "pending"
	partial = "partial"
	complete = "complete"
	error = "error"

