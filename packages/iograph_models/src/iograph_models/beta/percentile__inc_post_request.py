from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Percentile__incPostRequest(BaseModel):
	array: Optional[str] = Field(alias="array", default=None,)
	k: Optional[str] = Field(alias="k", default=None,)


