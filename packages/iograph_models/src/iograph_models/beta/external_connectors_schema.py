from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ExternalConnectorsSchema(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.externalConnectors.schema"] = Field(alias="@odata.type", default="#microsoft.graph.externalConnectors.schema")
	baseType: Optional[str] = Field(alias="baseType", default=None,)
	properties: Optional[list[ExternalConnectorsProperty]] = Field(alias="properties", default=None,)

from .external_connectors_property import ExternalConnectorsProperty
