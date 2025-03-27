from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class ExtractTransformation(BaseModel):
	input: Optional[TransformationAttribute] = Field(alias="input", default=None,)
	odata_type: Literal["#microsoft.graph.extractTransformation"] = Field(alias="@odata.type", default="#microsoft.graph.extractTransformation")
	type: Optional[str] = Field(alias="type", default=None,)
	value: Optional[str] = Field(alias="value", default=None,)
	value2: Optional[str] = Field(alias="value2", default=None,)

from .transformation_attribute import TransformationAttribute

