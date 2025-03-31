from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Generate_keyPostRequest(BaseModel):
	use: Optional[str] = Field(alias="use", default=None,)
	kty: Optional[str] = Field(alias="kty", default=None,)
	nbf: Optional[int] = Field(alias="nbf", default=None,)
	exp: Optional[int] = Field(alias="exp", default=None,)

