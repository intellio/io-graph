from __future__ import annotations
from enum import Enum


class AndroidWorkProfileRequiredPasswordType(Enum):
	deviceDefault = "deviceDefault"
	lowSecurityBiometric = "lowSecurityBiometric"
	required = "required"
	atLeastNumeric = "atLeastNumeric"
	numericComplex = "numericComplex"
	atLeastAlphabetic = "atLeastAlphabetic"
	atLeastAlphanumeric = "atLeastAlphanumeric"
	alphanumericWithSymbols = "alphanumericWithSymbols"

