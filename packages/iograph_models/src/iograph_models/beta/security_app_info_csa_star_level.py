from __future__ import annotations
from enum import StrEnum


class SecurityAppInfoCsaStarLevel(StrEnum):
	selfAssessment = "selfAssessment"
	certification = "certification"
	attestation = "attestation"
	cStarAssessment = "cStarAssessment"
	continuousMonitoring = "continuousMonitoring"
	unknown = "unknown"
	unknownFutureValue = "unknownFutureValue"

