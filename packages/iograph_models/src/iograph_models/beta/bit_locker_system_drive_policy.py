from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class BitLockerSystemDrivePolicy(BaseModel):
	encryptionMethod: Optional[BitLockerEncryptionMethod | str] = Field(alias="encryptionMethod", default=None,)
	minimumPinLength: Optional[int] = Field(alias="minimumPinLength", default=None,)
	prebootRecoveryEnableMessageAndUrl: Optional[bool] = Field(alias="prebootRecoveryEnableMessageAndUrl", default=None,)
	prebootRecoveryMessage: Optional[str] = Field(alias="prebootRecoveryMessage", default=None,)
	prebootRecoveryUrl: Optional[str] = Field(alias="prebootRecoveryUrl", default=None,)
	recoveryOptions: Optional[BitLockerRecoveryOptions] = Field(alias="recoveryOptions", default=None,)
	startupAuthenticationBlockWithoutTpmChip: Optional[bool] = Field(alias="startupAuthenticationBlockWithoutTpmChip", default=None,)
	startupAuthenticationRequired: Optional[bool] = Field(alias="startupAuthenticationRequired", default=None,)
	startupAuthenticationTpmKeyUsage: Optional[ConfigurationUsage | str] = Field(alias="startupAuthenticationTpmKeyUsage", default=None,)
	startupAuthenticationTpmPinAndKeyUsage: Optional[ConfigurationUsage | str] = Field(alias="startupAuthenticationTpmPinAndKeyUsage", default=None,)
	startupAuthenticationTpmPinUsage: Optional[ConfigurationUsage | str] = Field(alias="startupAuthenticationTpmPinUsage", default=None,)
	startupAuthenticationTpmUsage: Optional[ConfigurationUsage | str] = Field(alias="startupAuthenticationTpmUsage", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .bit_locker_encryption_method import BitLockerEncryptionMethod
from .bit_locker_recovery_options import BitLockerRecoveryOptions
from .configuration_usage import ConfigurationUsage
