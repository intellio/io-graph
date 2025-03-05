from __future__ import annotations
from enum import StrEnum


class TeamsAppDistributionMethod(StrEnum):
	store = "store"
	organization = "organization"
	sideloaded = "sideloaded"
	unknownFutureValue = "unknownFutureValue"

