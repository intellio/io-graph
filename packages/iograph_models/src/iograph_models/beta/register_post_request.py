from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RegisterPostRequest(BaseModel):
	externalId: Optional[str] = Field(alias="externalId", default=None,)

