from __future__ import annotations
from enum import Enum


class DefenderMonitorFileActivity(Enum):
	userDefined = "userDefined"
	disable = "disable"
	monitorAllFiles = "monitorAllFiles"
	monitorIncomingFilesOnly = "monitorIncomingFilesOnly"
	monitorOutgoingFilesOnly = "monitorOutgoingFilesOnly"

