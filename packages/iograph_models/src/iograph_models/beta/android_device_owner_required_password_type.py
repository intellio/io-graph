from __future__ import annotations
from enum import StrEnum


class AndroidDeviceOwnerRequiredPasswordType(StrEnum):
	deviceDefault = "deviceDefault"
	required = "required"
	numeric = "numeric"
	numericComplex = "numericComplex"
	alphabetic = "alphabetic"
	alphanumeric = "alphanumeric"
	alphanumericWithSymbols = "alphanumericWithSymbols"
	lowSecurityBiometric = "lowSecurityBiometric"
	customPassword = "customPassword"

