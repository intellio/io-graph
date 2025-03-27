from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityGovernanceCustomTaskExtensionCalloutData(BaseModel):
	odata_type: Literal["#microsoft.graph.identityGovernance.customTaskExtensionCalloutData"] = Field(alias="@odata.type", default="#microsoft.graph.identityGovernance.customTaskExtensionCalloutData")
	subject: Optional[User] = Field(alias="subject", default=None,)
	task: Optional[IdentityGovernanceTask] = Field(alias="task", default=None,)
	taskProcessingresult: Optional[IdentityGovernanceTaskProcessingResult] = Field(alias="taskProcessingresult", default=None,)
	workflow: Optional[IdentityGovernanceWorkflow] = Field(alias="workflow", default=None,)

from .user import User
from .identity_governance_task import IdentityGovernanceTask
from .identity_governance_task_processing_result import IdentityGovernanceTaskProcessingResult
from .identity_governance_workflow import IdentityGovernanceWorkflow

