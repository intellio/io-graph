from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RedirectUriSettings(BaseModel):
	index: Optional[int] = Field(alias="index", default=None,)
	uri: Optional[str] = Field(alias="uri", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


