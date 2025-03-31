from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class StartsWithTransformation(BaseModel):
	input: Optional[TransformationAttribute] = Field(alias="input", default=None,)
	odata_type: Literal["#microsoft.graph.startsWithTransformation"] = Field(alias="@odata.type", default="#microsoft.graph.startsWithTransformation")
	output: Optional[TransformationAttribute] = Field(alias="output", default=None,)
	value: Optional[str] = Field(alias="value", default=None,)

from .transformation_attribute import TransformationAttribute
