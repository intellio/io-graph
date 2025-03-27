from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class TooManyGlobalAdminsAssignedToTenantAlertIncident(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.tooManyGlobalAdminsAssignedToTenantAlertIncident"] = Field(alias="@odata.type", default="#microsoft.graph.tooManyGlobalAdminsAssignedToTenantAlertIncident")
	assigneeDisplayName: Optional[str] = Field(alias="assigneeDisplayName", default=None,)
	assigneeId: Optional[str] = Field(alias="assigneeId", default=None,)
	assigneeUserPrincipalName: Optional[str] = Field(alias="assigneeUserPrincipalName", default=None,)


