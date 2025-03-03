from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DeletedItemContainer(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	workflows: Optional[list[IdentityGovernanceWorkflow]] = Field(default=None,alias="workflows",)

from .identity_governance_workflow import IdentityGovernanceWorkflow

