from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ExternalConnectorsExternal(BaseModel):
	connections: Optional[list[ExternalConnectorsExternalConnection]] = Field(default=None,alias="connections",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .external_connectors_external_connection import ExternalConnectorsExternalConnection

