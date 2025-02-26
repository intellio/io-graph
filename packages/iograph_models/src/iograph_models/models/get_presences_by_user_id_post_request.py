from __future__ import annotations
from pydantic import BaseModel, Field


class Get_presences_by_user_idPostRequest(BaseModel):
	ids: list[str] = Field(alias="ids",)


