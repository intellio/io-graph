from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AttributeDefinitionMetadataEntry(BaseModel):
	key: Optional[AttributeDefinitionMetadata] = Field(default=None,alias="key",)
	value: Optional[str] = Field(default=None,alias="value",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .attribute_definition_metadata import AttributeDefinitionMetadata

