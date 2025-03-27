from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Sum_ifsPostRequest(BaseModel):
	sumRange: Optional[str] = Field(alias="sumRange", default=None,)
	values: Optional[str] = Field(alias="values", default=None,)


