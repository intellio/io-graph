from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class IdentityGovernanceTaskDefinition(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.identityGovernance.taskDefinition"] = Field(alias="@odata.type", default="#microsoft.graph.identityGovernance.taskDefinition")
	category: Optional[IdentityGovernanceLifecycleTaskCategory | str] = Field(alias="category", default=None,)
	continueOnError: Optional[bool] = Field(alias="continueOnError", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	parameters: Optional[list[IdentityGovernanceParameter]] = Field(alias="parameters", default=None,)
	version: Optional[int] = Field(alias="version", default=None,)

from .identity_governance_lifecycle_task_category import IdentityGovernanceLifecycleTaskCategory
from .identity_governance_parameter import IdentityGovernanceParameter
