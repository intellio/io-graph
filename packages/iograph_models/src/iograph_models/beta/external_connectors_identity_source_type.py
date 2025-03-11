from __future__ import annotations
from enum import StrEnum


class ExternalConnectorsIdentitySourceType(StrEnum):
	azureActiveDirectory = "azureActiveDirectory"
	external = "external"
	unknownFutureValue = "unknownFutureValue"

