from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class ExtractMailPrefixTransformation(BaseModel):
	input: Optional[TransformationAttribute] = Field(alias="input", default=None,)
	odata_type: Literal["#microsoft.graph.extractMailPrefixTransformation"] = Field(alias="@odata.type", default="#microsoft.graph.extractMailPrefixTransformation")

from .transformation_attribute import TransformationAttribute

