from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DelegatedAdminServiceManagementDetailCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[DelegatedAdminServiceManagementDetail]] = Field(default=None,alias="value",)

from .delegated_admin_service_management_detail import DelegatedAdminServiceManagementDetail

