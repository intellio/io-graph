from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ExpressionInputObject(BaseModel):
	definition: Optional[ObjectDefinition] = Field(alias="definition", default=None,)
	properties: Optional[list[StringKeyObjectValuePair]] = Field(alias="properties", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .object_definition import ObjectDefinition
from .string_key_object_value_pair import StringKeyObjectValuePair
