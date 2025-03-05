from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class FilterOperatorSchema(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	arity: Optional[ScopeOperatorType] = Field(default=None,alias="arity",)
	multivaluedComparisonType: Optional[ScopeOperatorMultiValuedComparisonType] = Field(default=None,alias="multivaluedComparisonType",)
	supportedAttributeTypes: Optional[list[AttributeType]] = Field(default=None,alias="supportedAttributeTypes",)

from .scope_operator_type import ScopeOperatorType
from .scope_operator_multi_valued_comparison_type import ScopeOperatorMultiValuedComparisonType
from .attribute_type import AttributeType

