from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class FilterClause(BaseModel):
	operatorName: Optional[str] = Field(default=None,alias="operatorName",)
	sourceOperandName: Optional[str] = Field(default=None,alias="sourceOperandName",)
	targetOperand: Optional[FilterOperand] = Field(default=None,alias="targetOperand",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .filter_operand import FilterOperand

