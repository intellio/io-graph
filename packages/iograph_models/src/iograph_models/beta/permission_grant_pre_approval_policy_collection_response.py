from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PermissionGrantPreApprovalPolicyCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[PermissionGrantPreApprovalPolicy]] = Field(alias="value", default=None,)

from .permission_grant_pre_approval_policy import PermissionGrantPreApprovalPolicy
