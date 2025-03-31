from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Confirm_safePostRequest(BaseModel):
	requestIds: Optional[list[str]] = Field(alias="requestIds", default=None,)

