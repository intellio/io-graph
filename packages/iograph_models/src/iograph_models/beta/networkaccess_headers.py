from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessHeaders(BaseModel):
	origin: Optional[str] = Field(alias="origin", default=None,)
	referrer: Optional[str] = Field(alias="referrer", default=None,)
	xForwardedFor: Optional[str] = Field(alias="xForwardedFor", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


