from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DelegatedAdminServiceManagementDetail(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	serviceManagementUrl: Optional[str] = Field(default=None,alias="serviceManagementUrl",)
	serviceName: Optional[str] = Field(default=None,alias="serviceName",)


