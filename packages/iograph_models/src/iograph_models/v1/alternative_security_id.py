from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AlternativeSecurityId(BaseModel):
	identityProvider: Optional[str] = Field(alias="identityProvider", default=None,)
	key: Optional[str] = Field(alias="key", default=None,)
	type: Optional[int] = Field(alias="type", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

