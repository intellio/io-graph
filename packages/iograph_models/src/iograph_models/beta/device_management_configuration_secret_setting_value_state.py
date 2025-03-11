from __future__ import annotations
from enum import StrEnum


class DeviceManagementConfigurationSecretSettingValueState(StrEnum):
	invalid = "invalid"
	notEncrypted = "notEncrypted"
	encryptedValueToken = "encryptedValueToken"

