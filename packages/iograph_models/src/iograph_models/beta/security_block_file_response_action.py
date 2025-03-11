from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityBlockFileResponseAction(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	deviceGroupNames: Optional[list[str]] = Field(alias="deviceGroupNames",default=None,)
	identifier: Optional[SecurityFileEntityIdentifier | str] = Field(alias="identifier",default=None,)

from .security_file_entity_identifier import SecurityFileEntityIdentifier

