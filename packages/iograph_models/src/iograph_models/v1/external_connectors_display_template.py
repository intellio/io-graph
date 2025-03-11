from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ExternalConnectorsDisplayTemplate(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	layout: Optional[str] = Field(alias="layout",default=None,)
	priority: Optional[int] = Field(alias="priority",default=None,)
	rules: Optional[list[ExternalConnectorsPropertyRule]] = Field(alias="rules",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .external_connectors_property_rule import ExternalConnectorsPropertyRule

