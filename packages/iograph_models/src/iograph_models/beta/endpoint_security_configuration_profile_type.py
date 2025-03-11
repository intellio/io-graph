from __future__ import annotations
from enum import StrEnum


class EndpointSecurityConfigurationProfileType(StrEnum):
	unknown = "unknown"
	antivirus = "antivirus"
	windowsSecurity = "windowsSecurity"
	bitLocker = "bitLocker"
	fileVault = "fileVault"
	firewall = "firewall"
	firewallRules = "firewallRules"
	endpointDetectionAndResponse = "endpointDetectionAndResponse"
	deviceControl = "deviceControl"
	appAndBrowserIsolation = "appAndBrowserIsolation"
	exploitProtection = "exploitProtection"
	webProtection = "webProtection"
	applicationControl = "applicationControl"
	attackSurfaceReductionRules = "attackSurfaceReductionRules"
	accountProtection = "accountProtection"

