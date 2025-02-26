from __future__ import annotations
from pydantic import BaseModel, Field


class Check_member_groupsPostRequest(BaseModel):
	groupIds: list[str] = Field(alias="groupIds",)


