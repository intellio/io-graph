from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ExternalConnectorsExternalActivityResult(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.externalConnectors.externalActivityResult"] = Field(alias="@odata.type", default="#microsoft.graph.externalConnectors.externalActivityResult")
	startDateTime: Optional[datetime] = Field(alias="startDateTime", default=None,)
	type: Optional[ExternalConnectorsExternalActivityType | str] = Field(alias="type", default=None,)
	performedBy: Optional[ExternalConnectorsIdentity] = Field(alias="performedBy", default=None,)
	error: Optional[PublicError] = Field(alias="error", default=None,)

from .external_connectors_external_activity_type import ExternalConnectorsExternalActivityType
from .external_connectors_identity import ExternalConnectorsIdentity
from .public_error import PublicError
