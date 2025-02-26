from __future__ import annotations
from enum import Enum


class AccessPackageExternalUserLifecycleAction(Enum):
	none = "none"
	blockSignIn = "blockSignIn"
	blockSignInAndDelete = "blockSignInAndDelete"
	unknownFutureValue = "unknownFutureValue"

