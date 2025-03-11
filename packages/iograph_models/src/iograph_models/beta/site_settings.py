from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SiteSettings(BaseModel):
	languageTag: Optional[str] = Field(alias="languageTag",default=None,)
	timeZone: Optional[str] = Field(alias="timeZone",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


