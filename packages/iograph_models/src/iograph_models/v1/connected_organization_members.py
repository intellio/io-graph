from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ConnectedOrganizationMembers(BaseModel):
	odata_type: Literal["#microsoft.graph.connectedOrganizationMembers"] = Field(alias="@odata.type", default="#microsoft.graph.connectedOrganizationMembers")
	connectedOrganizationId: Optional[str] = Field(alias="connectedOrganizationId", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)

