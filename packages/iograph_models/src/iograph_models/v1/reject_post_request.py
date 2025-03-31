from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RejectPostRequest(BaseModel):
	reason: Optional[RejectReason | str] = Field(alias="reason", default=None,)
	callbackUri: Optional[str] = Field(alias="callbackUri", default=None,)

from .reject_reason import RejectReason
