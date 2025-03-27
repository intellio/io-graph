from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SubstringTransformation(BaseModel):
	input: Optional[TransformationAttribute] = Field(alias="input", default=None,)
	odata_type: Literal["#microsoft.graph.substringTransformation"] = Field(alias="@odata.type", default="#microsoft.graph.substringTransformation")
	index: Optional[int] = Field(alias="index", default=None,)
	length: Optional[int] = Field(alias="length", default=None,)

from .transformation_attribute import TransformationAttribute

