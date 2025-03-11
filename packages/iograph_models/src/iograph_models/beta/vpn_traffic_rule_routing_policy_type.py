from __future__ import annotations
from enum import StrEnum


class VpnTrafficRuleRoutingPolicyType(StrEnum):
	none = "none"
	splitTunnel = "splitTunnel"
	forceTunnel = "forceTunnel"

