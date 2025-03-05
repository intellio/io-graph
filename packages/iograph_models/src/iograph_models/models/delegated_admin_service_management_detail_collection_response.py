from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DelegatedAdminServiceManagementDetailCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[DelegatedAdminServiceManagementDetail]] = Field(alias="value",default=None,)

from .delegated_admin_service_management_detail import DelegatedAdminServiceManagementDetail

