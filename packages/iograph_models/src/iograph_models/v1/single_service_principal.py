from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SingleServicePrincipal(BaseModel):
	odata_type: Literal["#microsoft.graph.singleServicePrincipal"] = Field(alias="@odata.type", default="#microsoft.graph.singleServicePrincipal")
	description: Optional[str] = Field(alias="description", default=None,)
	servicePrincipalId: Optional[str] = Field(alias="servicePrincipalId", default=None,)


