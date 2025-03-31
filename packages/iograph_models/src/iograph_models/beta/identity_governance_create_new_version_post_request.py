from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Identity_governance_create_new_versionPostRequest(BaseModel):
	workflow: Optional[IdentityGovernanceWorkflow] = Field(alias="workflow", default=None,)

from .identity_governance_workflow import IdentityGovernanceWorkflow
