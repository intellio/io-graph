from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserSecurityStateCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[UserSecurityState] = Field(alias="value",)

from .user_security_state import UserSecurityState

