from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class BitLockerFixedDrivePolicy(BaseModel):
	encryptionMethod: Optional[BitLockerEncryptionMethod | str] = Field(alias="encryptionMethod", default=None,)
	recoveryOptions: Optional[BitLockerRecoveryOptions] = Field(alias="recoveryOptions", default=None,)
	requireEncryptionForWriteAccess: Optional[bool] = Field(alias="requireEncryptionForWriteAccess", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .bit_locker_encryption_method import BitLockerEncryptionMethod
from .bit_locker_recovery_options import BitLockerRecoveryOptions

