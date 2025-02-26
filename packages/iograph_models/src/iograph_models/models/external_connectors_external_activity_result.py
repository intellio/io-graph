from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class ExternalConnectorsExternalActivityResult(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	startDateTime: Optional[datetime] = Field(default=None,alias="startDateTime",)
	type: Optional[ExternalConnectorsExternalActivityType] = Field(default=None,alias="type",)
	performedBy: Optional[ExternalConnectorsIdentity] = Field(default=None,alias="performedBy",)
	error: Optional[PublicError] = Field(default=None,alias="error",)

from .external_connectors_external_activity_type import ExternalConnectorsExternalActivityType
from .external_connectors_identity import ExternalConnectorsIdentity
from .public_error import PublicError

