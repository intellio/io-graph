from __future__ import annotations
from enum import StrEnum


class VpnOnDemandRuleInterfaceTypeMatch(StrEnum):
	notConfigured = "notConfigured"
	ethernet = "ethernet"
	wiFi = "wiFi"
	cellular = "cellular"

