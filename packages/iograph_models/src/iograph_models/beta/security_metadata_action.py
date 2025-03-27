from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityMetadataAction(BaseModel):
	odata_type: Literal["#microsoft.graph.security.metadataAction"] = Field(alias="@odata.type", default="#microsoft.graph.security.metadataAction")
	metadataToAdd: Optional[list[SecurityKeyValuePair]] = Field(alias="metadataToAdd", default=None,)
	metadataToRemove: Optional[list[str]] = Field(alias="metadataToRemove", default=None,)

from .security_key_value_pair import SecurityKeyValuePair

