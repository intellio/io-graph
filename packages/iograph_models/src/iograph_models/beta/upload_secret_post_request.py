from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Upload_secretPostRequest(BaseModel):
	use: Optional[str] = Field(alias="use", default=None,)
	k: Optional[str] = Field(alias="k", default=None,)
	nbf: Optional[int] = Field(alias="nbf", default=None,)
	exp: Optional[int] = Field(alias="exp", default=None,)


