from __future__ import annotations
from enum import StrEnum


class SharingScope(StrEnum):
	anyone = "anyone"
	organization = "organization"
	specificPeople = "specificPeople"
	anonymous = "anonymous"
	users = "users"
	unknownFutureValue = "unknownFutureValue"

