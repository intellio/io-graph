from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Create_sessionPostRequest(BaseModel):
	persistChanges: Optional[bool] = Field(default=None,alias="persistChanges",)


