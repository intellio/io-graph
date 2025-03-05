from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Norm__s__distPostRequest(BaseModel):
	z: Optional[str] = Field(alias="z",default=None,)
	cumulative: Optional[str] = Field(alias="cumulative",default=None,)


