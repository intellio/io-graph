from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class LocaleInfo(BaseModel):
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	locale: Optional[str] = Field(alias="locale", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


