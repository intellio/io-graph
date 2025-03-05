from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Chi_sq__dist__r_tPostRequest(BaseModel):
	x: Optional[str] = Field(default=None,alias="x",)
	degFreedom: Optional[str] = Field(default=None,alias="degFreedom",)


