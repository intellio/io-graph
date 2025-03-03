from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ExternalConnectorsDisplayTemplate(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	layout: Optional[str] = Field(default=None,alias="layout",)
	priority: Optional[int] = Field(default=None,alias="priority",)
	rules: Optional[list[ExternalConnectorsPropertyRule]] = Field(default=None,alias="rules",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .external_connectors_property_rule import ExternalConnectorsPropertyRule

