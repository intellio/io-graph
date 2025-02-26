from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Confirm_compromisedPostRequest(BaseModel):
	userIds: list[Optional[str]] = Field(alias="userIds",)


