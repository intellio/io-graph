from __future__ import annotations
from enum import StrEnum


class CloudAppSecuritySessionControlType(StrEnum):
	mcasConfigured = "mcasConfigured"
	monitorOnly = "monitorOnly"
	blockDownloads = "blockDownloads"
	unknownFutureValue = "unknownFutureValue"

