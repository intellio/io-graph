from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessRelatedTenant(BaseModel):
	odata_type: Literal["#microsoft.graph.networkaccess.relatedTenant"] = Field(alias="@odata.type", default="#microsoft.graph.networkaccess.relatedTenant")
	tenantId: Optional[str] = Field(alias="tenantId", default=None,)


