from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ExternalConnectorsExternalItem(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	acl: Optional[list[ExternalConnectorsAcl]] = Field(alias="acl",default=None,)
	content: Optional[ExternalConnectorsExternalItemContent] = Field(alias="content",default=None,)
	properties: Optional[ExternalConnectorsProperties] = Field(alias="properties",default=None,)
	activities: SerializeAsAny[Optional[list[ExternalConnectorsExternalActivity]]] = Field(alias="activities",default=None,)

from .external_connectors_acl import ExternalConnectorsAcl
from .external_connectors_external_item_content import ExternalConnectorsExternalItemContent
from .external_connectors_properties import ExternalConnectorsProperties
from .external_connectors_external_activity import ExternalConnectorsExternalActivity

