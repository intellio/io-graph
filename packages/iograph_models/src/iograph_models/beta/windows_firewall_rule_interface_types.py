from __future__ import annotations
from enum import StrEnum


class WindowsFirewallRuleInterfaceTypes(StrEnum):
	notConfigured = "notConfigured"
	remoteAccess = "remoteAccess"
	wireless = "wireless"
	lan = "lan"

