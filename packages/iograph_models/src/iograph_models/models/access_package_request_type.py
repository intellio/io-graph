from __future__ import annotations
from enum import StrEnum


class AccessPackageRequestType(StrEnum):
	notSpecified = "notSpecified"
	userAdd = "userAdd"
	userUpdate = "userUpdate"
	userRemove = "userRemove"
	adminAdd = "adminAdd"
	adminUpdate = "adminUpdate"
	adminRemove = "adminRemove"
	systemAdd = "systemAdd"
	systemUpdate = "systemUpdate"
	systemRemove = "systemRemove"
	onBehalfAdd = "onBehalfAdd"
	unknownFutureValue = "unknownFutureValue"

