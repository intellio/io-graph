from __future__ import annotations
from enum import StrEnum


class AppListType(StrEnum):
	none = "none"
	appsInListCompliant = "appsInListCompliant"
	appsNotInListCompliant = "appsNotInListCompliant"

