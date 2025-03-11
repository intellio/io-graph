from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AttributeMappingParameterSchema(BaseModel):
	allowMultipleOccurrences: Optional[bool] = Field(alias="allowMultipleOccurrences",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	required: Optional[bool] = Field(alias="required",default=None,)
	type: Optional[AttributeType | str] = Field(alias="type",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .attribute_type import AttributeType

