from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Im_realPostRequest(BaseModel):
	inumber: Optional[str] = Field(alias="inumber",default=None,)


