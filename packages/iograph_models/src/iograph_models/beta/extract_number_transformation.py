from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ExtractNumberTransformation(BaseModel):
	input: Optional[TransformationAttribute] = Field(alias="input",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	type: Optional[TransformationExtractType | str] = Field(alias="type",default=None,)

from .transformation_attribute import TransformationAttribute
from .transformation_extract_type import TransformationExtractType

