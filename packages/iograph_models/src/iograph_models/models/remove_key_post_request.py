from __future__ import annotations
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field


class Remove_keyPostRequest(BaseModel):
	keyId: Optional[UUID] = Field(default=None,alias="keyId",)
	proof: Optional[str] = Field(default=None,alias="proof",)


