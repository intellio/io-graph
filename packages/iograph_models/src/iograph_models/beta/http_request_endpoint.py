from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class HttpRequestEndpoint(BaseModel):
	odata_type: Literal["#microsoft.graph.httpRequestEndpoint"] = Field(alias="@odata.type", default="#microsoft.graph.httpRequestEndpoint")
	targetUrl: Optional[str] = Field(alias="targetUrl", default=None,)


