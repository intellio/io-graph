from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Sign_digestPostRequest(BaseModel):
	digest: Optional[str] = Field(alias="digest", default=None,)

