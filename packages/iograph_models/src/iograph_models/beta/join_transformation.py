from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class JoinTransformation(BaseModel):
	input: Optional[TransformationAttribute] = Field(alias="input",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	input2: Optional[TransformationAttribute] = Field(alias="input2",default=None,)
	separator: Optional[str] = Field(alias="separator",default=None,)

from .transformation_attribute import TransformationAttribute
from .transformation_attribute import TransformationAttribute

