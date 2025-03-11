from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class RedundantAssignmentAlertIncident(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	assigneeDisplayName: Optional[str] = Field(alias="assigneeDisplayName",default=None,)
	assigneeId: Optional[str] = Field(alias="assigneeId",default=None,)
	assigneeUserPrincipalName: Optional[str] = Field(alias="assigneeUserPrincipalName",default=None,)
	lastActivationDateTime: Optional[datetime] = Field(alias="lastActivationDateTime",default=None,)
	roleDefinitionId: Optional[str] = Field(alias="roleDefinitionId",default=None,)
	roleDisplayName: Optional[str] = Field(alias="roleDisplayName",default=None,)
	roleTemplateId: Optional[str] = Field(alias="roleTemplateId",default=None,)


