from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class HttpRequestEndpoint(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	targetUrl: Optional[str] = Field(alias="targetUrl",default=None,)


