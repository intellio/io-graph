from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IosWebContentFilterAutoFilter(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	allowedUrls: Optional[list[str]] = Field(alias="allowedUrls",default=None,)
	blockedUrls: Optional[list[str]] = Field(alias="blockedUrls",default=None,)


