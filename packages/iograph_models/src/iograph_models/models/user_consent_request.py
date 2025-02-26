from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class UserConsentRequest(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	approvalId: Optional[str] = Field(default=None,alias="approvalId",)
	completedDateTime: Optional[datetime] = Field(default=None,alias="completedDateTime",)
	createdBy: Optional[IdentitySet] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	customData: Optional[str] = Field(default=None,alias="customData",)
	status: Optional[str] = Field(default=None,alias="status",)
	reason: Optional[str] = Field(default=None,alias="reason",)
	approval: Optional[Approval] = Field(default=None,alias="approval",)

from .identity_set import IdentitySet
from .approval import Approval

