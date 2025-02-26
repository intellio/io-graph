from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IdentityGovernanceCustomTaskExtensionCalloutData(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	subject: Optional[User] = Field(default=None,alias="subject",)
	task: Optional[IdentityGovernanceTask] = Field(default=None,alias="task",)
	taskProcessingresult: Optional[IdentityGovernanceTaskProcessingResult] = Field(default=None,alias="taskProcessingresult",)
	workflow: Optional[IdentityGovernanceWorkflow] = Field(default=None,alias="workflow",)

from .user import User
from .identity_governance_task import IdentityGovernanceTask
from .identity_governance_task_processing_result import IdentityGovernanceTaskProcessingResult
from .identity_governance_workflow import IdentityGovernanceWorkflow

