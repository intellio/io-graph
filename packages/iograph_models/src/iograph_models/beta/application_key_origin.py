from __future__ import annotations
from enum import StrEnum


class ApplicationKeyOrigin(StrEnum):
	application = "application"
	servicePrincipal = "servicePrincipal"
	unknownFutureValue = "unknownFutureValue"

