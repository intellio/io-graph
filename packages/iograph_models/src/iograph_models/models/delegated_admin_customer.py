from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DelegatedAdminCustomer(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	tenantId: Optional[str] = Field(alias="tenantId",default=None,)
	serviceManagementDetails: Optional[list[DelegatedAdminServiceManagementDetail]] = Field(alias="serviceManagementDetails",default=None,)

from .delegated_admin_service_management_detail import DelegatedAdminServiceManagementDetail

