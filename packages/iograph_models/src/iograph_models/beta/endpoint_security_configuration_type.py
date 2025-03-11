from __future__ import annotations
from enum import StrEnum


class EndpointSecurityConfigurationType(StrEnum):
	unknown = "unknown"
	antivirus = "antivirus"
	diskEncryption = "diskEncryption"
	firewall = "firewall"
	endpointDetectionAndResponse = "endpointDetectionAndResponse"
	attackSurfaceReduction = "attackSurfaceReduction"
	accountProtection = "accountProtection"

