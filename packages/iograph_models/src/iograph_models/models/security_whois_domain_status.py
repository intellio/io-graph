from __future__ import annotations
from enum import Enum


class SecurityWhoisDomainStatus(Enum):
	clientDeleteProhibited = "clientDeleteProhibited"
	clientHold = "clientHold"
	clientRenewProhibited = "clientRenewProhibited"
	clientTransferProhibited = "clientTransferProhibited"
	clientUpdateProhibited = "clientUpdateProhibited"
	unknownFutureValue = "unknownFutureValue"

