from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcTenantEncryptionSetting(BaseModel):
	lastSyncDateTime: Optional[datetime] = Field(alias="lastSyncDateTime", default=None,)
	tenantDiskEncryptionType: Optional[CloudPcDiskEncryptionType | str] = Field(alias="tenantDiskEncryptionType", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .cloud_pc_disk_encryption_type import CloudPcDiskEncryptionType

