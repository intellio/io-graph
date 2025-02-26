from __future__ import annotations
from enum import Enum


class CloudAppSecuritySessionControlType(Enum):
	mcasConfigured = "mcasConfigured"
	monitorOnly = "monitorOnly"
	blockDownloads = "blockDownloads"
	unknownFutureValue = "unknownFutureValue"

