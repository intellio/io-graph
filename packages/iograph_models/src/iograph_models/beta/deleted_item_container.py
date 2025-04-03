from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DeletedItemContainer(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.deletedItemContainer"] = Field(alias="@odata.type", default="#microsoft.graph.deletedItemContainer")
	workflows: Optional[list[IdentityGovernanceWorkflow]] = Field(alias="workflows", default=None,)

from .identity_governance_workflow import IdentityGovernanceWorkflow
