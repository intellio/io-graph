from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ApprovalItemResponse(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.approvalItemResponse"] = Field(alias="@odata.type",)
	comments: Optional[str] = Field(alias="comments", default=None,)
	createdBy: Optional[ApprovalIdentitySet] = Field(alias="createdBy", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	owners: Optional[list[ApprovalIdentitySet]] = Field(alias="owners", default=None,)
	response: Optional[str] = Field(alias="response", default=None,)

from .approval_identity_set import ApprovalIdentitySet
