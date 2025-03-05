from __future__ import annotations
from enum import StrEnum


class AccessPackageSubjectType(StrEnum):
	notSpecified = "notSpecified"
	user = "user"
	servicePrincipal = "servicePrincipal"
	unknownFutureValue = "unknownFutureValue"

