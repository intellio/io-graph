from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Im_subPostRequest(BaseModel):
	inumber1: Optional[str] = Field(alias="inumber1",default=None,)
	inumber2: Optional[str] = Field(alias="inumber2",default=None,)


