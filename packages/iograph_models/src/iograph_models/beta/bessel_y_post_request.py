from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Bessel_yPostRequest(BaseModel):
	x: Optional[str] = Field(alias="x",default=None,)
	n: Optional[str] = Field(alias="n",default=None,)


