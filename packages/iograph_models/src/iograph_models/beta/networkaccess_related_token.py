from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessRelatedToken(BaseModel):
	odata_type: Literal["#microsoft.graph.networkaccess.relatedToken"] = Field(alias="@odata.type", default="#microsoft.graph.networkaccess.relatedToken")
	uniqueTokenIdentifier: Optional[str] = Field(alias="uniqueTokenIdentifier", default=None,)


