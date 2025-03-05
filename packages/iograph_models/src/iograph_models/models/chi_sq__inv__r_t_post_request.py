from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Chi_sq__inv__r_tPostRequest(BaseModel):
	probability: Optional[str] = Field(default=None,alias="probability",)
	degFreedom: Optional[str] = Field(default=None,alias="degFreedom",)


