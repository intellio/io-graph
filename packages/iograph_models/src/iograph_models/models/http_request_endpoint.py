from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class HttpRequestEndpoint(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	targetUrl: Optional[str] = Field(default=None,alias="targetUrl",)


