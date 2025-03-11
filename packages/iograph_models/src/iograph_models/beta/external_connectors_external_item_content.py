from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ExternalConnectorsExternalItemContent(BaseModel):
	type: Optional[ExternalConnectorsExternalItemContentType | str] = Field(alias="type",default=None,)
	value: Optional[str] = Field(alias="value",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .external_connectors_external_item_content_type import ExternalConnectorsExternalItemContentType

