from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RadiansPostRequest(BaseModel):
	angle: Optional[str] = Field(alias="angle", default=None,)

