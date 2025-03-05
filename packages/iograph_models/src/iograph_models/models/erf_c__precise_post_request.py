from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Erf_c__precisePostRequest(BaseModel):
	X: Optional[str] = Field(default=None,alias="X",)


