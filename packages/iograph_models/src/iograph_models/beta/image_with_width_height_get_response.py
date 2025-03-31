from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Image_with_width_heightGetResponse(BaseModel):
	value: Optional[str] = Field(alias="value", default=None,)

