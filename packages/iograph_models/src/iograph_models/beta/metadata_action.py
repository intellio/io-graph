from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MetadataAction(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	metadataToAdd: Optional[list[KeyValuePair]] = Field(alias="metadataToAdd",default=None,)
	metadataToRemove: Optional[list[str]] = Field(alias="metadataToRemove",default=None,)

from .key_value_pair import KeyValuePair

