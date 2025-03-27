from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AssignmentFilterSupportedProperty(BaseModel):
	dataType: Optional[str] = Field(alias="dataType", default=None,)
	isCollection: Optional[bool] = Field(alias="isCollection", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	propertyRegexConstraint: Optional[str] = Field(alias="propertyRegexConstraint", default=None,)
	supportedOperators: Optional[list[AssignmentFilterOperator | str]] = Field(alias="supportedOperators", default=None,)
	supportedValues: Optional[list[str]] = Field(alias="supportedValues", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .assignment_filter_operator import AssignmentFilterOperator

