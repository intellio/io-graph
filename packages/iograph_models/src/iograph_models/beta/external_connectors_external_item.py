from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import BaseModel, Field


class ExternalConnectorsExternalItem(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.externalConnectors.externalItem"] = Field(alias="@odata.type",)
	acl: Optional[list[ExternalConnectorsAcl]] = Field(alias="acl", default=None,)
	content: Optional[ExternalConnectorsExternalItemContent] = Field(alias="content", default=None,)
	properties: Optional[ExternalConnectorsProperties] = Field(alias="properties", default=None,)
	activities: Optional[list[Annotated[Union[ExternalConnectorsExternalActivityResult],Field(discriminator="odata_type")]]] = Field(alias="activities", default=None,)

from .external_connectors_acl import ExternalConnectorsAcl
from .external_connectors_external_item_content import ExternalConnectorsExternalItemContent
from .external_connectors_properties import ExternalConnectorsProperties
from .external_connectors_external_activity_result import ExternalConnectorsExternalActivityResult
