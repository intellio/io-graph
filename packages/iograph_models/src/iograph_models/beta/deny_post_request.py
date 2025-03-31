from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DenyPostRequest(BaseModel):
	reviewerJustification: Optional[str] = Field(alias="reviewerJustification", default=None,)

