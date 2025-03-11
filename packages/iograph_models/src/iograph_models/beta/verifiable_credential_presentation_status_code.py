from __future__ import annotations
from enum import StrEnum


class VerifiableCredentialPresentationStatusCode(StrEnum):
	request_retrieved = "request_retrieved"
	presentation_verified = "presentation_verified"
	unknownFutureValue = "unknownFutureValue"

