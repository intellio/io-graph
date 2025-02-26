from __future__ import annotations
from pydantic import BaseModel, Field


class Check_member_objectsPostRequest(BaseModel):
	ids: list[str] = Field(alias="ids",)


