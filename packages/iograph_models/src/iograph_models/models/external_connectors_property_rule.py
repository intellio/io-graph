from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ExternalConnectorsPropertyRule(BaseModel):
	operation: Optional[str | ExternalConnectorsRuleOperation] = Field(alias="operation",default=None,)
	property: Optional[str] = Field(alias="property",default=None,)
	values: Optional[list[str]] = Field(alias="values",default=None,)
	valuesJoinedBy: Optional[str | BinaryOperator] = Field(alias="valuesJoinedBy",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .external_connectors_rule_operation import ExternalConnectorsRuleOperation
from .binary_operator import BinaryOperator

