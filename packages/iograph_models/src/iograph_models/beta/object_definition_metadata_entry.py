from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ObjectDefinitionMetadataEntry(BaseModel):
	key: Optional[ObjectDefinitionMetadata | str] = Field(alias="key", default=None,)
	value: Optional[str] = Field(alias="value", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .object_definition_metadata import ObjectDefinitionMetadata

