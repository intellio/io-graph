from __future__ import annotations
from enum import StrEnum


class SamlNameIDFormat(StrEnum):
	default = "default"
	unspecified = "unspecified"
	emailAddress = "emailAddress"
	windowsDomainQualifiedName = "windowsDomainQualifiedName"
	persistent = "persistent"
	unknownFutureValue = "unknownFutureValue"

