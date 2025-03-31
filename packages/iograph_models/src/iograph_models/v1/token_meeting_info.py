from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class TokenMeetingInfo(BaseModel):
	odata_type: Literal["#microsoft.graph.tokenMeetingInfo"] = Field(alias="@odata.type", default="#microsoft.graph.tokenMeetingInfo")
	token: Optional[str] = Field(alias="token", default=None,)

