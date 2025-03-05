from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class T__dist_2_tPostRequest(BaseModel):
	x: Optional[str] = Field(default=None,alias="x",)
	degFreedom: Optional[str] = Field(default=None,alias="degFreedom",)


