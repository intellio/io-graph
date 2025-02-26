from __future__ import annotations
from enum import Enum


class AndroidRequiredPasswordType(Enum):
	deviceDefault = "deviceDefault"
	alphabetic = "alphabetic"
	alphanumeric = "alphanumeric"
	alphanumericWithSymbols = "alphanumericWithSymbols"
	lowSecurityBiometric = "lowSecurityBiometric"
	numeric = "numeric"
	numericComplex = "numericComplex"
	any = "any"

