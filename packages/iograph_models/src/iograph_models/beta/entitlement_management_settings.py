from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class EntitlementManagementSettings(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.entitlementManagementSettings"] = Field(alias="@odata.type", default="#microsoft.graph.entitlementManagementSettings")
	daysUntilExternalUserDeletedAfterBlocked: Optional[int] = Field(alias="daysUntilExternalUserDeletedAfterBlocked", default=None,)
	externalUserLifecycleAction: Optional[str] = Field(alias="externalUserLifecycleAction", default=None,)

