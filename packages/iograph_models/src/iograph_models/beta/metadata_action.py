from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class MetadataAction(BaseModel):
	odata_type: Literal["#microsoft.graph.metadataAction"] = Field(alias="@odata.type", default="#microsoft.graph.metadataAction")
	metadataToAdd: Optional[list[KeyValuePair]] = Field(alias="metadataToAdd", default=None,)
	metadataToRemove: Optional[list[str]] = Field(alias="metadataToRemove", default=None,)

from .key_value_pair import KeyValuePair

