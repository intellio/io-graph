from __future__ import annotations
from enum import StrEnum


class UserFlowType(StrEnum):
	signUp = "signUp"
	signIn = "signIn"
	signUpOrSignIn = "signUpOrSignIn"
	passwordReset = "passwordReset"
	profileUpdate = "profileUpdate"
	resourceOwner = "resourceOwner"
	unknownFutureValue = "unknownFutureValue"

