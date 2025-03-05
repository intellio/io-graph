from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ExternalConnectorsSchema(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	baseType: Optional[str] = Field(default=None,alias="baseType",)
	properties: Optional[list[ExternalConnectorsProperty]] = Field(default=None,alias="properties",)

from .external_connectors_property import ExternalConnectorsProperty

