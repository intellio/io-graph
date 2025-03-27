from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Chi_sq__invPostRequest(BaseModel):
	probability: Optional[str] = Field(alias="probability", default=None,)
	degFreedom: Optional[str] = Field(alias="degFreedom", default=None,)


