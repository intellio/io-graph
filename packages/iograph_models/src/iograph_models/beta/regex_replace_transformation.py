from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RegexReplaceTransformation(BaseModel):
	input: Optional[TransformationAttribute] = Field(alias="input",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	additionalAttributes: Optional[list[SourcedAttribute]] = Field(alias="additionalAttributes",default=None,)
	regex: Optional[str] = Field(alias="regex",default=None,)
	replacement: Optional[str] = Field(alias="replacement",default=None,)

from .transformation_attribute import TransformationAttribute
from .sourced_attribute import SourcedAttribute

