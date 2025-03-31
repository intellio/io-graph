from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class CustomSecurityAttributeStringValueExemption(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.customSecurityAttributeStringValueExemption"] = Field(alias="@odata.type", default="#microsoft.graph.customSecurityAttributeStringValueExemption")
	operator: Optional[CustomSecurityAttributeComparisonOperator | str] = Field(alias="operator", default=None,)
	value: Optional[str] = Field(alias="value", default=None,)

from .custom_security_attribute_comparison_operator import CustomSecurityAttributeComparisonOperator
