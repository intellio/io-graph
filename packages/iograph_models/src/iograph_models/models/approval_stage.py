from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ApprovalStage(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	assignedToMe: Optional[bool] = Field(alias="assignedToMe",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	justification: Optional[str] = Field(alias="justification",default=None,)
	reviewedBy: SerializeAsAny[Optional[Identity]] = Field(alias="reviewedBy",default=None,)
	reviewedDateTime: Optional[datetime] = Field(alias="reviewedDateTime",default=None,)
	reviewResult: Optional[str] = Field(alias="reviewResult",default=None,)
	status: Optional[str] = Field(alias="status",default=None,)

from .identity import Identity

