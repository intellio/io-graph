from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ExternalConnectorsIdentity(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.externalConnectors.identity"] = Field(alias="@odata.type",)
	type: Optional[ExternalConnectorsIdentityType | str] = Field(alias="type", default=None,)

from .external_connectors_identity_type import ExternalConnectorsIdentityType
