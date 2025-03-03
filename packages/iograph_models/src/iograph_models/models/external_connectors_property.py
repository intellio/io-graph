from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ExternalConnectorsProperty(BaseModel):
	aliases: Optional[list[str]] = Field(default=None,alias="aliases",)
	isQueryable: Optional[bool] = Field(default=None,alias="isQueryable",)
	isRefinable: Optional[bool] = Field(default=None,alias="isRefinable",)
	isRetrievable: Optional[bool] = Field(default=None,alias="isRetrievable",)
	isSearchable: Optional[bool] = Field(default=None,alias="isSearchable",)
	labels: Optional[ExternalConnectorsLabel] = Field(default=None,alias="labels",)
	name: Optional[str] = Field(default=None,alias="name",)
	type: Optional[ExternalConnectorsPropertyType] = Field(default=None,alias="type",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .external_connectors_label import ExternalConnectorsLabel
from .external_connectors_property_type import ExternalConnectorsPropertyType

