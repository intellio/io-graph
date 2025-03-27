from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Log_norm__invPostRequest(BaseModel):
	probability: Optional[str] = Field(alias="probability", default=None,)
	mean: Optional[str] = Field(alias="mean", default=None,)
	standardDev: Optional[str] = Field(alias="standardDev", default=None,)


