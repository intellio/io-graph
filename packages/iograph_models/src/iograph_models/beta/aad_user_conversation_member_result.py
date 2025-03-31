from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AadUserConversationMemberResult(BaseModel):
	error: Optional[PublicError] = Field(alias="error", default=None,)
	odata_type: Literal["#microsoft.graph.aadUserConversationMemberResult"] = Field(alias="@odata.type", default="#microsoft.graph.aadUserConversationMemberResult")
	userId: Optional[str] = Field(alias="userId", default=None,)

from .public_error import PublicError
