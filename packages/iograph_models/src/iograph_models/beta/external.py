from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class External(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.external"] = Field(alias="@odata.type",)
	connections: Optional[list[ExternalConnection]] = Field(alias="connections", default=None,)

from .external_connection import ExternalConnection
