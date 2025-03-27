from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Complete_setupPostRequest(BaseModel):
	tenantSetupInfo: Optional[TenantSetupInfo] = Field(alias="tenantSetupInfo", default=None,)

from .tenant_setup_info import TenantSetupInfo

