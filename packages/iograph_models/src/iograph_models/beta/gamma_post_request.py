from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class GammaPostRequest(BaseModel):
	x: Optional[str] = Field(alias="x",default=None,)


