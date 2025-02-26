from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Remove_groupPostRequest(BaseModel):
	groupId: Optional[str] = Field(default=None,alias="groupId",)


