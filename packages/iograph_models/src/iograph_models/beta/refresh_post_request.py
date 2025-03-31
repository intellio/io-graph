from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RefreshPostRequest(BaseModel):
	scopeType: Optional[str] = Field(alias="scopeType", default=None,)
	scopeId: Optional[str] = Field(alias="scopeId", default=None,)

