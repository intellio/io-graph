from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UnifiedStorageQuota(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	deleted: Optional[int] = Field(alias="deleted",default=None,)
	manageWebUrl: Optional[str] = Field(alias="manageWebUrl",default=None,)
	remaining: Optional[int] = Field(alias="remaining",default=None,)
	state: Optional[str] = Field(alias="state",default=None,)
	total: Optional[int] = Field(alias="total",default=None,)
	used: Optional[int] = Field(alias="used",default=None,)
	services: Optional[list[ServiceStorageQuotaBreakdown]] = Field(alias="services",default=None,)

from .service_storage_quota_breakdown import ServiceStorageQuotaBreakdown

