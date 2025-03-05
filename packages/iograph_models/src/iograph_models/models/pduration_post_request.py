from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PdurationPostRequest(BaseModel):
	rate: Optional[str] = Field(alias="rate",default=None,)
	pv: Optional[str] = Field(alias="pv",default=None,)
	fv: Optional[str] = Field(alias="fv",default=None,)


