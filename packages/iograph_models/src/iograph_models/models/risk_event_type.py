from __future__ import annotations
from enum import Enum


class RiskEventType(Enum):
	unlikelyTravel = "unlikelyTravel"
	anonymizedIPAddress = "anonymizedIPAddress"
	maliciousIPAddress = "maliciousIPAddress"
	unfamiliarFeatures = "unfamiliarFeatures"
	malwareInfectedIPAddress = "malwareInfectedIPAddress"
	suspiciousIPAddress = "suspiciousIPAddress"
	leakedCredentials = "leakedCredentials"
	investigationsThreatIntelligence = "investigationsThreatIntelligence"
	generic = "generic"
	adminConfirmedUserCompromised = "adminConfirmedUserCompromised"
	mcasImpossibleTravel = "mcasImpossibleTravel"
	mcasSuspiciousInboxManipulationRules = "mcasSuspiciousInboxManipulationRules"
	investigationsThreatIntelligenceSigninLinked = "investigationsThreatIntelligenceSigninLinked"
	maliciousIPAddressValidCredentialsBlockedIP = "maliciousIPAddressValidCredentialsBlockedIP"
	unknownFutureValue = "unknownFutureValue"

