from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class FilterClause(BaseModel):
	operatorName: Optional[str] = Field(alias="operatorName", default=None,)
	sourceOperandName: Optional[str] = Field(alias="sourceOperandName", default=None,)
	targetOperand: Optional[FilterOperand] = Field(alias="targetOperand", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .filter_operand import FilterOperand

