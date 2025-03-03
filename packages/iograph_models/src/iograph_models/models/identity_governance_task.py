from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IdentityGovernanceTask(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	arguments: Optional[list[KeyValuePair]] = Field(default=None,alias="arguments",)
	category: Optional[IdentityGovernanceLifecycleTaskCategory] = Field(default=None,alias="category",)
	continueOnError: Optional[bool] = Field(default=None,alias="continueOnError",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	executionSequence: Optional[int] = Field(default=None,alias="executionSequence",)
	isEnabled: Optional[bool] = Field(default=None,alias="isEnabled",)
	taskDefinitionId: Optional[str] = Field(default=None,alias="taskDefinitionId",)
	taskProcessingResults: Optional[list[IdentityGovernanceTaskProcessingResult]] = Field(default=None,alias="taskProcessingResults",)

from .key_value_pair import KeyValuePair
from .identity_governance_lifecycle_task_category import IdentityGovernanceLifecycleTaskCategory
from .identity_governance_task_processing_result import IdentityGovernanceTaskProcessingResult

