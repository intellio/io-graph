from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Set_verified_publisherPostRequest(BaseModel):
	verifiedPublisherId: Optional[str] = Field(default=None,alias="verifiedPublisherId",)


