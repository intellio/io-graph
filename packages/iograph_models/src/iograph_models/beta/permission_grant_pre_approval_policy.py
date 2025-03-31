from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class PermissionGrantPreApprovalPolicy(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.permissionGrantPreApprovalPolicy"] = Field(alias="@odata.type", default="#microsoft.graph.permissionGrantPreApprovalPolicy")
	deletedDateTime: Optional[datetime] = Field(alias="deletedDateTime", default=None,)
	conditions: Optional[list[PreApprovalDetail]] = Field(alias="conditions", default=None,)

from .pre_approval_detail import PreApprovalDetail
