from __future__ import annotations
from enum import StrEnum


class DefenderMonitorFileActivity(StrEnum):
	userDefined = "userDefined"
	disable = "disable"
	monitorAllFiles = "monitorAllFiles"
	monitorIncomingFilesOnly = "monitorIncomingFilesOnly"
	monitorOutgoingFilesOnly = "monitorOutgoingFilesOnly"

