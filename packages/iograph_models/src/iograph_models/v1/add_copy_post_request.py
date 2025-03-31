from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Add_copyPostRequest(BaseModel):
	contentType: Optional[str] = Field(alias="contentType", default=None,)

