from __future__ import annotations
from enum import StrEnum


class OnPremisesPublishingType(StrEnum):
	applicationProxy = "applicationProxy"
	exchangeOnline = "exchangeOnline"
	authentication = "authentication"
	provisioning = "provisioning"
	intunePfx = "intunePfx"
	oflineDomainJoin = "oflineDomainJoin"
	unknownFutureValue = "unknownFutureValue"

