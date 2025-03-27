from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Settings(BaseModel):
	hasGraphMailbox: Optional[bool] = Field(alias="hasGraphMailbox", default=None,)
	hasLicense: Optional[bool] = Field(alias="hasLicense", default=None,)
	hasOptedOut: Optional[bool] = Field(alias="hasOptedOut", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


