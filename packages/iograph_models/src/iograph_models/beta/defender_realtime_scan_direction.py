from __future__ import annotations
from enum import StrEnum


class DefenderRealtimeScanDirection(StrEnum):
	monitorAllFiles = "monitorAllFiles"
	monitorIncomingFilesOnly = "monitorIncomingFilesOnly"
	monitorOutgoingFilesOnly = "monitorOutgoingFilesOnly"

