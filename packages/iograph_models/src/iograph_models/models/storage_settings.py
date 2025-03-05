from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class StorageSettings(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	quota: Optional[UnifiedStorageQuota] = Field(default=None,alias="quota",)

from .unified_storage_quota import UnifiedStorageQuota

