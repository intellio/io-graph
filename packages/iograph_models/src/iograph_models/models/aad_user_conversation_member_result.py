from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AadUserConversationMemberResult(BaseModel):
	error: Optional[PublicError] = Field(default=None,alias="error",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	userId: Optional[str] = Field(default=None,alias="userId",)

from .public_error import PublicError

