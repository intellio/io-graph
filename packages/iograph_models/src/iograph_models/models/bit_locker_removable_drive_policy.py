from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class BitLockerRemovableDrivePolicy(BaseModel):
	blockCrossOrganizationWriteAccess: Optional[bool] = Field(default=None,alias="blockCrossOrganizationWriteAccess",)
	encryptionMethod: Optional[BitLockerEncryptionMethod] = Field(default=None,alias="encryptionMethod",)
	requireEncryptionForWriteAccess: Optional[bool] = Field(default=None,alias="requireEncryptionForWriteAccess",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .bit_locker_encryption_method import BitLockerEncryptionMethod

