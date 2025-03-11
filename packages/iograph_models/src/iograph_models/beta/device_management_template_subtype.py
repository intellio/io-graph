from __future__ import annotations
from enum import StrEnum


class DeviceManagementTemplateSubtype(StrEnum):
	none = "none"
	firewall = "firewall"
	diskEncryption = "diskEncryption"
	attackSurfaceReduction = "attackSurfaceReduction"
	endpointDetectionReponse = "endpointDetectionReponse"
	accountProtection = "accountProtection"
	antivirus = "antivirus"
	firewallSharedAppList = "firewallSharedAppList"
	firewallSharedIpList = "firewallSharedIpList"
	firewallSharedPortlist = "firewallSharedPortlist"

