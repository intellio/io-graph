from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessRelatedUrl(BaseModel):
	odata_type: Literal["#microsoft.graph.networkaccess.relatedUrl"] = Field(alias="@odata.type", default="#microsoft.graph.networkaccess.relatedUrl")
	url: Optional[str] = Field(alias="url", default=None,)


