from __future__ import annotations
from enum import StrEnum


class DeviceManagementConfigurationSettingAccessTypes(StrEnum):
	none = "none"
	add = "add"
	copy = "copy"
	delete = "delete"
	get = "get"
	replace = "replace"
	execute = "execute"

