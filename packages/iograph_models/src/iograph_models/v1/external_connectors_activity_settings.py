from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ExternalConnectorsActivitySettings(BaseModel):
	urlToItemResolvers: SerializeAsAny[Optional[list[ExternalConnectorsUrlToItemResolverBase]]] = Field(alias="urlToItemResolvers",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .external_connectors_url_to_item_resolver_base import ExternalConnectorsUrlToItemResolverBase

