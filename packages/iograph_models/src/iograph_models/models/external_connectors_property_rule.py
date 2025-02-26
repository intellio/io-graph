from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ExternalConnectorsPropertyRule(BaseModel):
	operation: Optional[ExternalConnectorsRuleOperation] = Field(default=None,alias="operation",)
	property: Optional[str] = Field(default=None,alias="property",)
	values: list[str] = Field(alias="values",)
	valuesJoinedBy: Optional[BinaryOperator] = Field(default=None,alias="valuesJoinedBy",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .external_connectors_rule_operation import ExternalConnectorsRuleOperation
from .binary_operator import BinaryOperator

