from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class External(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	connections: Optional[list[ExternalConnection]] = Field(alias="connections",default=None,)

from .external_connection import ExternalConnection

