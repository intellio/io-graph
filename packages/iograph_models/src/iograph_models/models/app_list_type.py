from __future__ import annotations
from enum import Enum


class AppListType(Enum):
	none = "none"
	appsInListCompliant = "appsInListCompliant"
	appsNotInListCompliant = "appsNotInListCompliant"

