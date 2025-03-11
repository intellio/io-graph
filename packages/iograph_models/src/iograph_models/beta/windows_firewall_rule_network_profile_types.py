from __future__ import annotations
from enum import StrEnum


class WindowsFirewallRuleNetworkProfileTypes(StrEnum):
	notConfigured = "notConfigured"
	domain = "domain"
	private = "private"
	public = "public"

