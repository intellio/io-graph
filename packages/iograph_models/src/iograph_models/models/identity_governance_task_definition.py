from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IdentityGovernanceTaskDefinition(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	category: Optional[IdentityGovernanceLifecycleTaskCategory] = Field(default=None,alias="category",)
	continueOnError: Optional[bool] = Field(default=None,alias="continueOnError",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	parameters: list[IdentityGovernanceParameter] = Field(alias="parameters",)
	version: Optional[int] = Field(default=None,alias="version",)

from .identity_governance_lifecycle_task_category import IdentityGovernanceLifecycleTaskCategory
from .identity_governance_parameter import IdentityGovernanceParameter

