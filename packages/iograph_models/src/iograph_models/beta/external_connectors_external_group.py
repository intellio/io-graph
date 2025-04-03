from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ExternalConnectorsExternalGroup(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.externalConnectors.externalGroup"] = Field(alias="@odata.type", default="#microsoft.graph.externalConnectors.externalGroup")
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	members: Optional[list[ExternalConnectorsIdentity]] = Field(alias="members", default=None,)

from .external_connectors_identity import ExternalConnectorsIdentity
