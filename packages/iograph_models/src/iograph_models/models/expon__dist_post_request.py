from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Expon__distPostRequest(BaseModel):
	x: Optional[str] = Field(default=None,alias="x",)
	lambda_: Optional[str] = Field(default=None,alias="lambda",)
	cumulative: Optional[str] = Field(default=None,alias="cumulative",)


