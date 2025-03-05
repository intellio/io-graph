from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityGovernanceTaskProcessingResult(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	completedDateTime: Optional[datetime] = Field(default=None,alias="completedDateTime",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	failureReason: Optional[str] = Field(default=None,alias="failureReason",)
	processingStatus: Optional[IdentityGovernanceLifecycleWorkflowProcessingStatus] = Field(default=None,alias="processingStatus",)
	startedDateTime: Optional[datetime] = Field(default=None,alias="startedDateTime",)
	subject: Optional[User] = Field(default=None,alias="subject",)
	task: Optional[IdentityGovernanceTask] = Field(default=None,alias="task",)

from .identity_governance_lifecycle_workflow_processing_status import IdentityGovernanceLifecycleWorkflowProcessingStatus
from .user import User
from .identity_governance_task import IdentityGovernanceTask

