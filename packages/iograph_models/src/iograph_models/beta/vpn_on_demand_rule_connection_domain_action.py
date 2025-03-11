from __future__ import annotations
from enum import StrEnum


class VpnOnDemandRuleConnectionDomainAction(StrEnum):
	connectIfNeeded = "connectIfNeeded"
	neverConnect = "neverConnect"

