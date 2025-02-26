from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ExternalConnectorsExternalItem(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	acl: list[ExternalConnectorsAcl] = Field(alias="acl",)
	content: Optional[ExternalConnectorsExternalItemContent] = Field(default=None,alias="content",)
	properties: Optional[ExternalConnectorsProperties] = Field(default=None,alias="properties",)
	activities: list[ExternalConnectorsExternalActivity] = Field(alias="activities",)

from .external_connectors_acl import ExternalConnectorsAcl
from .external_connectors_external_item_content import ExternalConnectorsExternalItemContent
from .external_connectors_properties import ExternalConnectorsProperties
from .external_connectors_external_activity import ExternalConnectorsExternalActivity

