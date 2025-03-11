from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ExternalConnectorsExternalActivityCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: SerializeAsAny[Optional[list[ExternalConnectorsExternalActivity]]] = Field(alias="value",default=None,)

from .external_connectors_external_activity import ExternalConnectorsExternalActivity

