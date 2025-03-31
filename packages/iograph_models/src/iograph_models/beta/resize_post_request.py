from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ResizePostRequest(BaseModel):
	targetServicePlanId: Optional[str] = Field(alias="targetServicePlanId", default=None,)

