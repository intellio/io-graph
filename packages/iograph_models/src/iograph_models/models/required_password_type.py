from __future__ import annotations
from enum import StrEnum


class RequiredPasswordType(StrEnum):
	deviceDefault = "deviceDefault"
	alphanumeric = "alphanumeric"
	numeric = "numeric"

