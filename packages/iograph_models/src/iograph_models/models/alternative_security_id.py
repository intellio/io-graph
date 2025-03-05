from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AlternativeSecurityId(BaseModel):
	identityProvider: Optional[str] = Field(default=None,alias="identityProvider",)
	key: Optional[str] = Field(default=None,alias="key",)
	type: Optional[int] = Field(default=None,alias="type",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


