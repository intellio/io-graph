from __future__ import annotations
from enum import StrEnum


class AndroidRequiredPasswordType(StrEnum):
	deviceDefault = "deviceDefault"
	alphabetic = "alphabetic"
	alphanumeric = "alphanumeric"
	alphanumericWithSymbols = "alphanumericWithSymbols"
	lowSecurityBiometric = "lowSecurityBiometric"
	numeric = "numeric"
	numericComplex = "numericComplex"
	any = "any"

