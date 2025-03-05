from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ExternalConnectorsIdentity(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	type: Optional[ExternalConnectorsIdentityType] = Field(default=None,alias="type",)

from .external_connectors_identity_type import ExternalConnectorsIdentityType

