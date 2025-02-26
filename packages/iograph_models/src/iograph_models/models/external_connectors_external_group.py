from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ExternalConnectorsExternalGroup(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	members: list[ExternalConnectorsIdentity] = Field(alias="members",)

from .external_connectors_identity import ExternalConnectorsIdentity

