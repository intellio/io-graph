from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ExternalConnectorsSearchSettings(BaseModel):
	searchResultTemplates: list[ExternalConnectorsDisplayTemplate] = Field(alias="searchResultTemplates",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .external_connectors_display_template import ExternalConnectorsDisplayTemplate

