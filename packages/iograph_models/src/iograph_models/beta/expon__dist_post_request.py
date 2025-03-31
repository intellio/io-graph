from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Expon__distPostRequest(BaseModel):
	x: Optional[str] = Field(alias="x", default=None,)
	lambda_: Optional[str] = Field(alias="lambda", default=None,)
	cumulative: Optional[str] = Field(alias="cumulative", default=None,)

