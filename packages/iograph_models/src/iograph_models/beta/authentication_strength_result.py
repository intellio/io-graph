from __future__ import annotations
from enum import StrEnum


class AuthenticationStrengthResult(StrEnum):
	notSet = "notSet"
	skippedForProofUp = "skippedForProofUp"
	satisfied = "satisfied"
	singleChallengeRequired = "singleChallengeRequired"
	multipleChallengesRequired = "multipleChallengesRequired"
	singleRegistrationRequired = "singleRegistrationRequired"
	multipleRegistrationsRequired = "multipleRegistrationsRequired"
	cannotSatisfyDueToCombinationConfiguration = "cannotSatisfyDueToCombinationConfiguration"
	cannotSatisfy = "cannotSatisfy"
	unknownFutureValue = "unknownFutureValue"

