from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SubstringTransformation(BaseModel):
	input: Optional[TransformationAttribute] = Field(alias="input",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	index: Optional[int] = Field(alias="index",default=None,)
	length: Optional[int] = Field(alias="length",default=None,)

from .transformation_attribute import TransformationAttribute

