from __future__ import annotations
from enum import Enum


class RecipientScopeType(Enum):
	none = "none"
	internal = "internal"
	external = "external"
	externalPartner = "externalPartner"
	externalNonPartner = "externalNonPartner"

