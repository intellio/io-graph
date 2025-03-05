from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Gamma_ln__precisePostRequest(BaseModel):
	x: Optional[str] = Field(default=None,alias="x",)


