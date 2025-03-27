from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class IfEmptyTransformation(BaseModel):
	input: Optional[TransformationAttribute] = Field(alias="input", default=None,)
	odata_type: Literal["#microsoft.graph.ifEmptyTransformation"] = Field(alias="@odata.type", default="#microsoft.graph.ifEmptyTransformation")
	output: Optional[TransformationAttribute] = Field(alias="output", default=None,)

from .transformation_attribute import TransformationAttribute
from .transformation_attribute import TransformationAttribute

