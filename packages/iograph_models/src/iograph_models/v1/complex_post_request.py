from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ComplexPostRequest(BaseModel):
	realNum: Optional[str] = Field(alias="realNum",default=None,)
	iNum: Optional[str] = Field(alias="iNum",default=None,)
	suffix: Optional[str] = Field(alias="suffix",default=None,)


