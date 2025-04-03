from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class StorageSettings(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.storageSettings"] = Field(alias="@odata.type", default="#microsoft.graph.storageSettings")
	quota: Optional[UnifiedStorageQuota] = Field(alias="quota", default=None,)

from .unified_storage_quota import UnifiedStorageQuota
