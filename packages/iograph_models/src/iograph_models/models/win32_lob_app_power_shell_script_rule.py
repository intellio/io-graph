from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Win32LobAppPowerShellScriptRule(BaseModel):
	ruleType: Optional[Win32LobAppRuleType] = Field(default=None,alias="ruleType",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	comparisonValue: Optional[str] = Field(default=None,alias="comparisonValue",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	enforceSignatureCheck: Optional[bool] = Field(default=None,alias="enforceSignatureCheck",)
	operationType: Optional[Win32LobAppPowerShellScriptRuleOperationType] = Field(default=None,alias="operationType",)
	operator: Optional[Win32LobAppRuleOperator] = Field(default=None,alias="operator",)
	runAs32Bit: Optional[bool] = Field(default=None,alias="runAs32Bit",)
	runAsAccount: Optional[RunAsAccountType] = Field(default=None,alias="runAsAccount",)
	scriptContent: Optional[str] = Field(default=None,alias="scriptContent",)

from .win32_lob_app_rule_type import Win32LobAppRuleType
from .win32_lob_app_power_shell_script_rule_operation_type import Win32LobAppPowerShellScriptRuleOperationType
from .win32_lob_app_rule_operator import Win32LobAppRuleOperator
from .run_as_account_type import RunAsAccountType

