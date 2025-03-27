from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Coup_pcdPostRequest(BaseModel):
	settlement: Optional[str] = Field(alias="settlement", default=None,)
	maturity: Optional[str] = Field(alias="maturity", default=None,)
	frequency: Optional[str] = Field(alias="frequency", default=None,)
	basis: Optional[str] = Field(alias="basis", default=None,)


