from __future__ import annotations
from enum import StrEnum


class DerivedCredentialProviderType(StrEnum):
	notConfigured = "notConfigured"
	entrustDataCard = "entrustDataCard"
	purebred = "purebred"
	xTec = "xTec"
	intercede = "intercede"

