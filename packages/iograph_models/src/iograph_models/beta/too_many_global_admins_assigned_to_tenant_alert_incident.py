from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TooManyGlobalAdminsAssignedToTenantAlertIncident(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	assigneeDisplayName: Optional[str] = Field(alias="assigneeDisplayName",default=None,)
	assigneeId: Optional[str] = Field(alias="assigneeId",default=None,)
	assigneeUserPrincipalName: Optional[str] = Field(alias="assigneeUserPrincipalName",default=None,)


