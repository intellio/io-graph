from __future__ import annotations
from enum import Enum


class TeamsAppDistributionMethod(Enum):
	store = "store"
	organization = "organization"
	sideloaded = "sideloaded"
	unknownFutureValue = "unknownFutureValue"

