from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Accr_int_mPostRequest(BaseModel):
	issue: Optional[str] = Field(alias="issue",default=None,)
	settlement: Optional[str] = Field(alias="settlement",default=None,)
	rate: Optional[str] = Field(alias="rate",default=None,)
	par: Optional[str] = Field(alias="par",default=None,)
	basis: Optional[str] = Field(alias="basis",default=None,)


