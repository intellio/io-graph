from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ExternalConnectorsUrlToItemResolverBaseCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: SerializeAsAny[Optional[list[ExternalConnectorsUrlToItemResolverBase]]] = Field(alias="value",default=None,)

from .external_connectors_url_to_item_resolver_base import ExternalConnectorsUrlToItemResolverBase

