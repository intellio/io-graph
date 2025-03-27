from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class FilterOperatorSchema(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	arity: Optional[ScopeOperatorType | str] = Field(alias="arity", default=None,)
	multivaluedComparisonType: Optional[ScopeOperatorMultiValuedComparisonType | str] = Field(alias="multivaluedComparisonType", default=None,)
	supportedAttributeTypes: Optional[list[AttributeType | str]] = Field(alias="supportedAttributeTypes", default=None,)

from .scope_operator_type import ScopeOperatorType
from .scope_operator_multi_valued_comparison_type import ScopeOperatorMultiValuedComparisonType
from .attribute_type import AttributeType

