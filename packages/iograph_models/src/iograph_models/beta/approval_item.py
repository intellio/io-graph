from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ApprovalItem(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.approvalItem"] = Field(alias="@odata.type", default="#microsoft.graph.approvalItem")
	allowCancel: Optional[bool] = Field(alias="allowCancel", default=None,)
	allowEmailNotification: Optional[bool] = Field(alias="allowEmailNotification", default=None,)
	approvalType: Optional[ApprovalItemType | str] = Field(alias="approvalType", default=None,)
	approvers: Optional[list[ApprovalIdentitySet]] = Field(alias="approvers", default=None,)
	completedDateTime: Optional[datetime] = Field(alias="completedDateTime", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	owner: Optional[ApprovalIdentitySet] = Field(alias="owner", default=None,)
	responsePrompts: Optional[list[str]] = Field(alias="responsePrompts", default=None,)
	result: Optional[str] = Field(alias="result", default=None,)
	state: Optional[ApprovalItemState | str] = Field(alias="state", default=None,)
	viewPoint: Optional[ApprovalItemViewPoint] = Field(alias="viewPoint", default=None,)
	requests: Optional[list[ApprovalItemRequest]] = Field(alias="requests", default=None,)
	responses: Optional[list[ApprovalItemResponse]] = Field(alias="responses", default=None,)

from .approval_item_type import ApprovalItemType
from .approval_identity_set import ApprovalIdentitySet
from .approval_item_state import ApprovalItemState
from .approval_item_view_point import ApprovalItemViewPoint
from .approval_item_request import ApprovalItemRequest
from .approval_item_response import ApprovalItemResponse
