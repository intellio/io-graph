from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class ServicePrincipalSubject(BaseModel):
	odata_type: Literal["#microsoft.graph.servicePrincipalSubject"] = Field(alias="@odata.type", default="#microsoft.graph.servicePrincipalSubject")
	servicePrincipalId: Optional[str] = Field(alias="servicePrincipalId", default=None,)


