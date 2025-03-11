from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Apply_custom_filterPostRequest(BaseModel):
	criteria1: Optional[str] = Field(alias="criteria1",default=None,)
	criteria2: Optional[str] = Field(alias="criteria2",default=None,)
	oper: Optional[str] = Field(alias="oper",default=None,)


