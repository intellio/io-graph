from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CloudPcBulkModifyDiskEncryptionTypeCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[CloudPcBulkModifyDiskEncryptionType]] = Field(alias="value", default=None,)

from .cloud_pc_bulk_modify_disk_encryption_type import CloudPcBulkModifyDiskEncryptionType
