from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DelegatedAdminCustomer(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	tenantId: Optional[str] = Field(default=None,alias="tenantId",)
	serviceManagementDetails: list[DelegatedAdminServiceManagementDetail] = Field(alias="serviceManagementDetails",)

from .delegated_admin_service_management_detail import DelegatedAdminServiceManagementDetail

