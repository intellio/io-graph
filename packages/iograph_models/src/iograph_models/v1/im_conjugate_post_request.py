from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Im_conjugatePostRequest(BaseModel):
	inumber: Optional[str] = Field(alias="inumber", default=None,)

