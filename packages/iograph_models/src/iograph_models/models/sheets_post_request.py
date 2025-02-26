from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SheetsPostRequest(BaseModel):
	reference: Optional[str] = Field(default=None,alias="reference",)


