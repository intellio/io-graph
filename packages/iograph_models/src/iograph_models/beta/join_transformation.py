from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class JoinTransformation(BaseModel):
	input: Optional[TransformationAttribute] = Field(alias="input", default=None,)
	odata_type: Literal["#microsoft.graph.joinTransformation"] = Field(alias="@odata.type", default="#microsoft.graph.joinTransformation")
	input2: Optional[TransformationAttribute] = Field(alias="input2", default=None,)
	separator: Optional[str] = Field(alias="separator", default=None,)

from .transformation_attribute import TransformationAttribute
from .transformation_attribute import TransformationAttribute

