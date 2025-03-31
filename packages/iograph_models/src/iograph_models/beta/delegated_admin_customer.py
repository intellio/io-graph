from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DelegatedAdminCustomer(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.delegatedAdminCustomer"] = Field(alias="@odata.type",)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	tenantId: Optional[str] = Field(alias="tenantId", default=None,)
	serviceManagementDetails: Optional[list[DelegatedAdminServiceManagementDetail]] = Field(alias="serviceManagementDetails", default=None,)

from .delegated_admin_service_management_detail import DelegatedAdminServiceManagementDetail
