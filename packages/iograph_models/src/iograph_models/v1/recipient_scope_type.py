from __future__ import annotations
from enum import StrEnum


class RecipientScopeType(StrEnum):
	none = "none"
	internal = "internal"
	external = "external"
	externalPartner = "externalPartner"
	externalNonPartner = "externalNonPartner"

