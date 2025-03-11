from __future__ import annotations
from enum import StrEnum


class SharingRole(StrEnum):
	none = "none"
	view = "view"
	edit = "edit"
	manageList = "manageList"
	review = "review"
	restrictedView = "restrictedView"
	submitOnly = "submitOnly"
	unknownFutureValue = "unknownFutureValue"

