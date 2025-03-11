from __future__ import annotations
from enum import StrEnum


class AndroidWorkProfileRequiredPasswordType(StrEnum):
	deviceDefault = "deviceDefault"
	lowSecurityBiometric = "lowSecurityBiometric"
	required = "required"
	atLeastNumeric = "atLeastNumeric"
	numericComplex = "numericComplex"
	atLeastAlphabetic = "atLeastAlphabetic"
	atLeastAlphanumeric = "atLeastAlphanumeric"
	alphanumericWithSymbols = "alphanumericWithSymbols"

