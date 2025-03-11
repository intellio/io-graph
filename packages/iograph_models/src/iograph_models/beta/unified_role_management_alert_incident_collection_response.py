from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UnifiedRoleManagementAlertIncidentCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: SerializeAsAny[Optional[list[UnifiedRoleManagementAlertIncident]]] = Field(alias="value",default=None,)

from .unified_role_management_alert_incident import UnifiedRoleManagementAlertIncident

