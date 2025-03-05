from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Win32LobAppRegistryRule(BaseModel):
	ruleType: Optional[Win32LobAppRuleType] = Field(default=None,alias="ruleType",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	check32BitOn64System: Optional[bool] = Field(default=None,alias="check32BitOn64System",)
	comparisonValue: Optional[str] = Field(default=None,alias="comparisonValue",)
	keyPath: Optional[str] = Field(default=None,alias="keyPath",)
	operationType: Optional[Win32LobAppRegistryRuleOperationType] = Field(default=None,alias="operationType",)
	operator: Optional[Win32LobAppRuleOperator] = Field(default=None,alias="operator",)
	valueName: Optional[str] = Field(default=None,alias="valueName",)

from .win32_lob_app_rule_type import Win32LobAppRuleType
from .win32_lob_app_registry_rule_operation_type import Win32LobAppRegistryRuleOperationType
from .win32_lob_app_rule_operator import Win32LobAppRuleOperator

