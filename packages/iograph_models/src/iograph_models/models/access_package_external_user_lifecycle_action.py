from __future__ import annotations
from enum import StrEnum


class AccessPackageExternalUserLifecycleAction(StrEnum):
	none = "none"
	blockSignIn = "blockSignIn"
	blockSignInAndDelete = "blockSignInAndDelete"
	unknownFutureValue = "unknownFutureValue"

