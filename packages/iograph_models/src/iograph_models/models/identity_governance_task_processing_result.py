from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityGovernanceTaskProcessingResult(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	completedDateTime: Optional[datetime] = Field(alias="completedDateTime",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	failureReason: Optional[str] = Field(alias="failureReason",default=None,)
	processingStatus: Optional[str | IdentityGovernanceLifecycleWorkflowProcessingStatus] = Field(alias="processingStatus",default=None,)
	startedDateTime: Optional[datetime] = Field(alias="startedDateTime",default=None,)
	subject: Optional[User] = Field(alias="subject",default=None,)
	task: Optional[IdentityGovernanceTask] = Field(alias="task",default=None,)

from .identity_governance_lifecycle_workflow_processing_status import IdentityGovernanceLifecycleWorkflowProcessingStatus
from .user import User
from .identity_governance_task import IdentityGovernanceTask

