from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ExternalConnectorsSearchSettings(BaseModel):
	searchResultTemplates: Optional[list[ExternalConnectorsDisplayTemplate]] = Field(alias="searchResultTemplates", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .external_connectors_display_template import ExternalConnectorsDisplayTemplate

