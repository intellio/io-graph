from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ApprovalWorkflowProviderCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[ApprovalWorkflowProvider]] = Field(alias="value",default=None,)

from .approval_workflow_provider import ApprovalWorkflowProvider

