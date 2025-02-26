from __future__ import annotations
from enum import Enum


class AccessPackageSubjectType(Enum):
	notSpecified = "notSpecified"
	user = "user"
	servicePrincipal = "servicePrincipal"
	unknownFutureValue = "unknownFutureValue"

