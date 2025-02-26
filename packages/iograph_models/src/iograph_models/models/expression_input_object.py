from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ExpressionInputObject(BaseModel):
	definition: Optional[ObjectDefinition] = Field(default=None,alias="definition",)
	properties: list[StringKeyObjectValuePair] = Field(alias="properties",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .object_definition import ObjectDefinition
from .string_key_object_value_pair import StringKeyObjectValuePair

