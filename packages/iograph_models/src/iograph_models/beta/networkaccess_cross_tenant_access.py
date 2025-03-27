from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessCrossTenantAccess(BaseModel):
	deviceCount: Optional[int] = Field(alias="deviceCount", default=None,)
	lastAccessDateTime: Optional[datetime] = Field(alias="lastAccessDateTime", default=None,)
	resourceTenantId: Optional[str] = Field(alias="resourceTenantId", default=None,)
	resourceTenantName: Optional[str] = Field(alias="resourceTenantName", default=None,)
	resourceTenantPrimaryDomain: Optional[str] = Field(alias="resourceTenantPrimaryDomain", default=None,)
	usageStatus: Optional[NetworkaccessUsageStatus | str] = Field(alias="usageStatus", default=None,)
	userCount: Optional[int] = Field(alias="userCount", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .networkaccess_usage_status import NetworkaccessUsageStatus

