from __future__ import annotations
from enum import StrEnum


class IdentitySourceType(StrEnum):
	azureActiveDirectory = "azureActiveDirectory"
	external = "external"

