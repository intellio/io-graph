from __future__ import annotations
from enum import Enum


class FederatedIdpMfaBehavior(Enum):
	acceptIfMfaDoneByFederatedIdp = "acceptIfMfaDoneByFederatedIdp"
	enforceMfaByFederatedIdp = "enforceMfaByFederatedIdp"
	rejectMfaByFederatedIdp = "rejectMfaByFederatedIdp"
	unknownFutureValue = "unknownFutureValue"

