from __future__ import annotations
from enum import StrEnum


class ClassificationMethod(StrEnum):
	patternMatch = "patternMatch"
	exactDataMatch = "exactDataMatch"
	fingerprint = "fingerprint"
	machineLearning = "machineLearning"

