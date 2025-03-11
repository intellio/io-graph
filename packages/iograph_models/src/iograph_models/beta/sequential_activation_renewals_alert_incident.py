from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SequentialActivationRenewalsAlertIncident(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	activationCount: Optional[int] = Field(alias="activationCount",default=None,)
	assigneeDisplayName: Optional[str] = Field(alias="assigneeDisplayName",default=None,)
	assigneeId: Optional[str] = Field(alias="assigneeId",default=None,)
	assigneeUserPrincipalName: Optional[str] = Field(alias="assigneeUserPrincipalName",default=None,)
	roleDefinitionId: Optional[str] = Field(alias="roleDefinitionId",default=None,)
	roleDisplayName: Optional[str] = Field(alias="roleDisplayName",default=None,)
	roleTemplateId: Optional[str] = Field(alias="roleTemplateId",default=None,)
	sequenceEndDateTime: Optional[datetime] = Field(alias="sequenceEndDateTime",default=None,)
	sequenceStartDateTime: Optional[datetime] = Field(alias="sequenceStartDateTime",default=None,)


