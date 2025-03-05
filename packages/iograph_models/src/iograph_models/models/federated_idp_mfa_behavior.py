from __future__ import annotations
from enum import StrEnum


class FederatedIdpMfaBehavior(StrEnum):
	acceptIfMfaDoneByFederatedIdp = "acceptIfMfaDoneByFederatedIdp"
	enforceMfaByFederatedIdp = "enforceMfaByFederatedIdp"
	rejectMfaByFederatedIdp = "rejectMfaByFederatedIdp"
	unknownFutureValue = "unknownFutureValue"

