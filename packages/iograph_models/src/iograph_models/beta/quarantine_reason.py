from __future__ import annotations
from enum import StrEnum


class QuarantineReason(StrEnum):
	EncounteredBaseEscrowThreshold = "EncounteredBaseEscrowThreshold"
	EncounteredTotalEscrowThreshold = "EncounteredTotalEscrowThreshold"
	EncounteredEscrowProportionThreshold = "EncounteredEscrowProportionThreshold"
	EncounteredQuarantineException = "EncounteredQuarantineException"
	Unknown = "Unknown"
	QuarantinedOnDemand = "QuarantinedOnDemand"
	TooManyDeletes = "TooManyDeletes"
	IngestionInterrupted = "IngestionInterrupted"

