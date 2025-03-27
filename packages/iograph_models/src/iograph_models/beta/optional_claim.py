from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OptionalClaim(BaseModel):
	additionalProperties: Optional[list[str]] = Field(alias="additionalProperties", default=None,)
	essential: Optional[bool] = Field(alias="essential", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	source: Optional[str] = Field(alias="source", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


