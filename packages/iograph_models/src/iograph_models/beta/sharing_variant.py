from __future__ import annotations
from enum import StrEnum


class SharingVariant(StrEnum):
	none = "none"
	requiresAuthentication = "requiresAuthentication"
	passwordProtected = "passwordProtected"
	addressBar = "addressBar"
	embed = "embed"
	unknownFutureValue = "unknownFutureValue"

