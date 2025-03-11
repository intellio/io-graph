from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ExternalConnectorsSchema(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	baseType: Optional[str] = Field(alias="baseType",default=None,)
	properties: Optional[list[ExternalConnectorsProperty]] = Field(alias="properties",default=None,)

from .external_connectors_property import ExternalConnectorsProperty

