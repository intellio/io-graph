from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ExternalConnectorsExternal(BaseModel):
	connections: Optional[list[ExternalConnectorsExternalConnection]] = Field(alias="connections",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .external_connectors_external_connection import ExternalConnectorsExternalConnection

