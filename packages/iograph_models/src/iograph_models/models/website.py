from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Website(BaseModel):
	address: Optional[str] = Field(alias="address",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	type: Optional[str | WebsiteType] = Field(alias="type",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .website_type import WebsiteType

