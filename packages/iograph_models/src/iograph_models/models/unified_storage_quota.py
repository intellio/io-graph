from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UnifiedStorageQuota(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	deleted: Optional[int] = Field(default=None,alias="deleted",)
	manageWebUrl: Optional[str] = Field(default=None,alias="manageWebUrl",)
	remaining: Optional[int] = Field(default=None,alias="remaining",)
	state: Optional[str] = Field(default=None,alias="state",)
	total: Optional[int] = Field(default=None,alias="total",)
	used: Optional[int] = Field(default=None,alias="used",)
	services: Optional[list[ServiceStorageQuotaBreakdown]] = Field(default=None,alias="services",)

from .service_storage_quota_breakdown import ServiceStorageQuotaBreakdown

