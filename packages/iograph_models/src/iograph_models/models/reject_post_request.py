from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RejectPostRequest(BaseModel):
	reason: Optional[RejectReason] = Field(default=None,alias="reason",)
	callbackUri: Optional[str] = Field(default=None,alias="callbackUri",)

from .reject_reason import RejectReason

