from __future__ import annotations
from enum import Enum


class UserFlowType(Enum):
	signUp = "signUp"
	signIn = "signIn"
	signUpOrSignIn = "signUpOrSignIn"
	passwordReset = "passwordReset"
	profileUpdate = "profileUpdate"
	resourceOwner = "resourceOwner"
	unknownFutureValue = "unknownFutureValue"

