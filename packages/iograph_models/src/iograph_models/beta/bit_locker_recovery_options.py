from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class BitLockerRecoveryOptions(BaseModel):
	blockDataRecoveryAgent: Optional[bool] = Field(alias="blockDataRecoveryAgent",default=None,)
	enableBitLockerAfterRecoveryInformationToStore: Optional[bool] = Field(alias="enableBitLockerAfterRecoveryInformationToStore",default=None,)
	enableRecoveryInformationSaveToStore: Optional[bool] = Field(alias="enableRecoveryInformationSaveToStore",default=None,)
	hideRecoveryOptions: Optional[bool] = Field(alias="hideRecoveryOptions",default=None,)
	recoveryInformationToStore: Optional[BitLockerRecoveryInformationType | str] = Field(alias="recoveryInformationToStore",default=None,)
	recoveryKeyUsage: Optional[ConfigurationUsage | str] = Field(alias="recoveryKeyUsage",default=None,)
	recoveryPasswordUsage: Optional[ConfigurationUsage | str] = Field(alias="recoveryPasswordUsage",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .bit_locker_recovery_information_type import BitLockerRecoveryInformationType
from .configuration_usage import ConfigurationUsage
from .configuration_usage import ConfigurationUsage

