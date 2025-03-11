from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CustomSecurityAttributeStringValueExemption(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	operator: Optional[CustomSecurityAttributeComparisonOperator | str] = Field(alias="operator",default=None,)
	value: Optional[str] = Field(alias="value",default=None,)

from .custom_security_attribute_comparison_operator import CustomSecurityAttributeComparisonOperator

