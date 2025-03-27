from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeletedItemContainer(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	workflows: Optional[list[IdentityGovernanceWorkflow]] = Field(alias="workflows", default=None,)

from .identity_governance_workflow import IdentityGovernanceWorkflow

