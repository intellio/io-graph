from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Add_groupPostRequest(BaseModel):
	groupId: Optional[str] = Field(alias="groupId", default=None,)

