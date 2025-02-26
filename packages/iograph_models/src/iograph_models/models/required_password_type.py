from __future__ import annotations
from enum import Enum


class RequiredPasswordType(Enum):
	deviceDefault = "deviceDefault"
	alphanumeric = "alphanumeric"
	numeric = "numeric"

