from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class F__inv__r_tPostRequest(BaseModel):
	probability: Optional[str] = Field(default=None,alias="probability",)
	degFreedom1: Optional[str] = Field(default=None,alias="degFreedom1",)
	degFreedom2: Optional[str] = Field(default=None,alias="degFreedom2",)


