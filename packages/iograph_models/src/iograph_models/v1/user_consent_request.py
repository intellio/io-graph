from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class UserConsentRequest(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	approvalId: Optional[str] = Field(alias="approvalId",default=None,)
	completedDateTime: Optional[datetime] = Field(alias="completedDateTime",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	customData: Optional[str] = Field(alias="customData",default=None,)
	status: Optional[str] = Field(alias="status",default=None,)
	reason: Optional[str] = Field(alias="reason",default=None,)
	approval: Optional[Approval] = Field(alias="approval",default=None,)

from .identity_set import IdentitySet
from .approval import Approval

