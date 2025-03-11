from __future__ import annotations
from enum import StrEnum


class PartnerTenantType(StrEnum):
	microsoftSupport = "microsoftSupport"
	syndicatePartner = "syndicatePartner"
	breadthPartner = "breadthPartner"
	breadthPartnerDelegatedAdmin = "breadthPartnerDelegatedAdmin"
	resellerPartnerDelegatedAdmin = "resellerPartnerDelegatedAdmin"
	valueAddedResellerPartnerDelegatedAdmin = "valueAddedResellerPartnerDelegatedAdmin"
	unknownFutureValue = "unknownFutureValue"

