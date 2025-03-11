from __future__ import annotations
from enum import StrEnum


class MobileThreatDefensePartnerPriority(StrEnum):
	defenderOverThirdPartyPartner = "defenderOverThirdPartyPartner"
	thirdPartyPartnerOverDefender = "thirdPartyPartnerOverDefender"
	unknownFutureValue = "unknownFutureValue"

