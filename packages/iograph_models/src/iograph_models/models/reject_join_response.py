from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RejectJoinResponse(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	reason: Optional[str | RejectReason] = Field(alias="reason",default=None,)

from .reject_reason import RejectReason

