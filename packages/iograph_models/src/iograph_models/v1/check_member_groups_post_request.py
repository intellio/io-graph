from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Check_member_groupsPostRequest(BaseModel):
	groupIds: Optional[list[str]] = Field(alias="groupIds", default=None,)

