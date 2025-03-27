from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Chi_sq__dist__r_tPostRequest(BaseModel):
	x: Optional[str] = Field(alias="x", default=None,)
	degFreedom: Optional[str] = Field(alias="degFreedom", default=None,)


