from __future__ import annotations
from enum import StrEnum


class NetworkaccessAlertType(StrEnum):
	unhealthyRemoteNetworks = "unhealthyRemoteNetworks"
	unhealthyConnectors = "unhealthyConnectors"
	deviceTokenInconsistency = "deviceTokenInconsistency"
	crossTenantAnomaly = "crossTenantAnomaly"
	suspiciousProcess = "suspiciousProcess"
	threatIntelligenceTransactions = "threatIntelligenceTransactions"
	unknownFutureValue = "unknownFutureValue"
	webContentBlocked = "webContentBlocked"
	malware = "malware"
	patientZero = "patientZero"
	dlp = "dlp"

