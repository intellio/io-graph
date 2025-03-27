from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class TrimTransformation(BaseModel):
	input: Optional[TransformationAttribute] = Field(alias="input", default=None,)
	odata_type: Literal["#microsoft.graph.trimTransformation"] = Field(alias="@odata.type", default="#microsoft.graph.trimTransformation")
	type: Optional[TransformationTrimType | str] = Field(alias="type", default=None,)
	value: Optional[str] = Field(alias="value", default=None,)

from .transformation_attribute import TransformationAttribute
from .transformation_trim_type import TransformationTrimType

