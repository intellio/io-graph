from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class IdentityGovernanceTask(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.identityGovernance.task"] = Field(alias="@odata.type",)
	arguments: Optional[list[KeyValuePair]] = Field(alias="arguments", default=None,)
	category: Optional[IdentityGovernanceLifecycleTaskCategory | str] = Field(alias="category", default=None,)
	continueOnError: Optional[bool] = Field(alias="continueOnError", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	executionSequence: Optional[int] = Field(alias="executionSequence", default=None,)
	isEnabled: Optional[bool] = Field(alias="isEnabled", default=None,)
	taskDefinitionId: Optional[str] = Field(alias="taskDefinitionId", default=None,)
	taskProcessingResults: Optional[list[IdentityGovernanceTaskProcessingResult]] = Field(alias="taskProcessingResults", default=None,)

from .key_value_pair import KeyValuePair
from .identity_governance_lifecycle_task_category import IdentityGovernanceLifecycleTaskCategory
from .identity_governance_task_processing_result import IdentityGovernanceTaskProcessingResult
