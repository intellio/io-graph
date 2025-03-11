from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class StartsWithTransformation(BaseModel):
	input: Optional[TransformationAttribute] = Field(alias="input",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	output: Optional[TransformationAttribute] = Field(alias="output",default=None,)
	value: Optional[str] = Field(alias="value",default=None,)

from .transformation_attribute import TransformationAttribute
from .transformation_attribute import TransformationAttribute

