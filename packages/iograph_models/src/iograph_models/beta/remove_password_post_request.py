from __future__ import annotations
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field


class Remove_passwordPostRequest(BaseModel):
	keyId: Optional[UUID] = Field(alias="keyId", default=None,)

