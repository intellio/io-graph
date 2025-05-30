from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ToLowercaseTransformation(BaseModel):
	input: Optional[TransformationAttribute] = Field(alias="input", default=None,)
	odata_type: Literal["#microsoft.graph.toLowercaseTransformation"] = Field(alias="@odata.type", default="#microsoft.graph.toLowercaseTransformation")

from .transformation_attribute import TransformationAttribute
