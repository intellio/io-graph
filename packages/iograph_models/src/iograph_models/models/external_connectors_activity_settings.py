from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ExternalConnectorsActivitySettings(BaseModel):
	urlToItemResolvers: Optional[list[ExternalConnectorsUrlToItemResolverBase]] = Field(default=None,alias="urlToItemResolvers",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .external_connectors_url_to_item_resolver_base import ExternalConnectorsUrlToItemResolverBase

