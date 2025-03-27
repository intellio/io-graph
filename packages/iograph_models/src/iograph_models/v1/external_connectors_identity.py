from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ExternalConnectorsIdentity(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	type: Optional[ExternalConnectorsIdentityType | str] = Field(alias="type", default=None,)

from .external_connectors_identity_type import ExternalConnectorsIdentityType

