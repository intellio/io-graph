from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcForensicStorageAccount(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	accessTier: Optional[CloudPcStorageAccountAccessTier | str] = Field(alias="accessTier",default=None,)
	immutableStorage: Optional[bool] = Field(alias="immutableStorage",default=None,)
	storageAccountId: Optional[str] = Field(alias="storageAccountId",default=None,)
	storageAccountName: Optional[str] = Field(alias="storageAccountName",default=None,)

from .cloud_pc_storage_account_access_tier import CloudPcStorageAccountAccessTier

