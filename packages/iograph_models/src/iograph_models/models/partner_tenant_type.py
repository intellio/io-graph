from __future__ import annotations
from enum import Enum


class PartnerTenantType(Enum):
	microsoftSupport = "microsoftSupport"
	syndicatePartner = "syndicatePartner"
	breadthPartner = "breadthPartner"
	breadthPartnerDelegatedAdmin = "breadthPartnerDelegatedAdmin"
	resellerPartnerDelegatedAdmin = "resellerPartnerDelegatedAdmin"
	valueAddedResellerPartnerDelegatedAdmin = "valueAddedResellerPartnerDelegatedAdmin"
	unknownFutureValue = "unknownFutureValue"

