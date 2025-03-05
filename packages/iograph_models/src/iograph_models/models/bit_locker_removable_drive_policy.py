from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class BitLockerRemovableDrivePolicy(BaseModel):
	blockCrossOrganizationWriteAccess: Optional[bool] = Field(alias="blockCrossOrganizationWriteAccess",default=None,)
	encryptionMethod: Optional[str | BitLockerEncryptionMethod] = Field(alias="encryptionMethod",default=None,)
	requireEncryptionForWriteAccess: Optional[bool] = Field(alias="requireEncryptionForWriteAccess",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .bit_locker_encryption_method import BitLockerEncryptionMethod

