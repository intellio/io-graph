from __future__ import annotations
from enum import StrEnum


class WindowsFirewallRuleTrafficDirectionType(StrEnum):
	notConfigured = "notConfigured"
	out = "out"
	in_ = "in_"

