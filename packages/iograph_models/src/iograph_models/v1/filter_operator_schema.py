from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class FilterOperatorSchema(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.filterOperatorSchema"] = Field(alias="@odata.type", default="#microsoft.graph.filterOperatorSchema")
	arity: Optional[ScopeOperatorType | str] = Field(alias="arity", default=None,)
	multivaluedComparisonType: Optional[ScopeOperatorMultiValuedComparisonType | str] = Field(alias="multivaluedComparisonType", default=None,)
	supportedAttributeTypes: Optional[list[AttributeType | str]] = Field(alias="supportedAttributeTypes", default=None,)

from .scope_operator_type import ScopeOperatorType
from .scope_operator_multi_valued_comparison_type import ScopeOperatorMultiValuedComparisonType
from .attribute_type import AttributeType
