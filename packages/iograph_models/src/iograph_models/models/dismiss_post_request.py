from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DismissPostRequest(BaseModel):
	userIds: list[Optional[str]] = Field(alias="userIds",)


