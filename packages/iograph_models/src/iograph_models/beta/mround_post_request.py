from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MroundPostRequest(BaseModel):
	number: Optional[str] = Field(alias="number",default=None,)
	multiple: Optional[str] = Field(alias="multiple",default=None,)


