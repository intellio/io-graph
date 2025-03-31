from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class RejectJoinResponse(BaseModel):
	odata_type: Literal["#microsoft.graph.rejectJoinResponse"] = Field(alias="@odata.type", default="#microsoft.graph.rejectJoinResponse")
	reason: Optional[RejectReason | str] = Field(alias="reason", default=None,)

from .reject_reason import RejectReason
