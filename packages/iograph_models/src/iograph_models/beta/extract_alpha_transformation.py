from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class ExtractAlphaTransformation(BaseModel):
	input: Optional[TransformationAttribute] = Field(alias="input", default=None,)
	odata_type: Literal["#microsoft.graph.extractAlphaTransformation"] = Field(alias="@odata.type", default="#microsoft.graph.extractAlphaTransformation")
	type: Optional[TransformationExtractType | str] = Field(alias="type", default=None,)

from .transformation_attribute import TransformationAttribute
from .transformation_extract_type import TransformationExtractType

