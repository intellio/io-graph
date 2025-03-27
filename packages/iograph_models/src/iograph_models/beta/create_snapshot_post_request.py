from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Create_snapshotPostRequest(BaseModel):
	storageAccountId: Optional[str] = Field(alias="storageAccountId", default=None,)
	accessTier: Optional[CloudPcBlobAccessTier | str] = Field(alias="accessTier", default=None,)

from .cloud_pc_blob_access_tier import CloudPcBlobAccessTier

