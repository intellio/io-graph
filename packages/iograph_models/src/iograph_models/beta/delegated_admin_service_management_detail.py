from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DelegatedAdminServiceManagementDetail(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.delegatedAdminServiceManagementDetail"] = Field(alias="@odata.type", default="#microsoft.graph.delegatedAdminServiceManagementDetail")
	serviceManagementUrl: Optional[str] = Field(alias="serviceManagementUrl", default=None,)
	serviceName: Optional[str] = Field(alias="serviceName", default=None,)

