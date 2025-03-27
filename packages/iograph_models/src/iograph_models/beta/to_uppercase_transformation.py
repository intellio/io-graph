from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class ToUppercaseTransformation(BaseModel):
	input: Optional[TransformationAttribute] = Field(alias="input", default=None,)
	odata_type: Literal["#microsoft.graph.toUppercaseTransformation"] = Field(alias="@odata.type", default="#microsoft.graph.toUppercaseTransformation")

from .transformation_attribute import TransformationAttribute

