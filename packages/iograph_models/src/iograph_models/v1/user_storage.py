from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserStorage(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	quota: Optional[UnifiedStorageQuota] = Field(alias="quota",default=None,)

from .unified_storage_quota import UnifiedStorageQuota

