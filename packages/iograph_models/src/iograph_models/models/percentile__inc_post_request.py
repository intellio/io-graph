from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Percentile__incPostRequest(BaseModel):
	array: Optional[str] = Field(default=None,alias="array",)
	k: Optional[str] = Field(default=None,alias="k",)


