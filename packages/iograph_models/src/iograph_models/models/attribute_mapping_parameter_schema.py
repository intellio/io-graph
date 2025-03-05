from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AttributeMappingParameterSchema(BaseModel):
	allowMultipleOccurrences: Optional[bool] = Field(default=None,alias="allowMultipleOccurrences",)
	name: Optional[str] = Field(default=None,alias="name",)
	required: Optional[bool] = Field(default=None,alias="required",)
	type: Optional[AttributeType] = Field(default=None,alias="type",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .attribute_type import AttributeType

