from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RejectPostRequest(BaseModel):
	reason: Optional[str | RejectReason] = Field(alias="reason",default=None,)
	callbackUri: Optional[str] = Field(alias="callbackUri",default=None,)

from .reject_reason import RejectReason

