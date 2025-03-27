from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Norm__s__invPostRequest(BaseModel):
	probability: Optional[str] = Field(alias="probability", default=None,)


