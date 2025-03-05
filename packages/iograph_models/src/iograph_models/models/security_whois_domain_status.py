from __future__ import annotations
from enum import StrEnum


class SecurityWhoisDomainStatus(StrEnum):
	clientDeleteProhibited = "clientDeleteProhibited"
	clientHold = "clientHold"
	clientRenewProhibited = "clientRenewProhibited"
	clientTransferProhibited = "clientTransferProhibited"
	clientUpdateProhibited = "clientUpdateProhibited"
	unknownFutureValue = "unknownFutureValue"

