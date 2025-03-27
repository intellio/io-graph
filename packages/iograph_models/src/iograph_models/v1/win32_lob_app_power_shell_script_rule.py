from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class Win32LobAppPowerShellScriptRule(BaseModel):
	ruleType: Optional[Win32LobAppRuleType | str] = Field(alias="ruleType", default=None,)
	odata_type: Literal["#microsoft.graph.win32LobAppPowerShellScriptRule"] = Field(alias="@odata.type", default="#microsoft.graph.win32LobAppPowerShellScriptRule")
	comparisonValue: Optional[str] = Field(alias="comparisonValue", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	enforceSignatureCheck: Optional[bool] = Field(alias="enforceSignatureCheck", default=None,)
	operationType: Optional[Win32LobAppPowerShellScriptRuleOperationType | str] = Field(alias="operationType", default=None,)
	operator: Optional[Win32LobAppRuleOperator | str] = Field(alias="operator", default=None,)
	runAs32Bit: Optional[bool] = Field(alias="runAs32Bit", default=None,)
	runAsAccount: Optional[RunAsAccountType | str] = Field(alias="runAsAccount", default=None,)
	scriptContent: Optional[str] = Field(alias="scriptContent", default=None,)

from .win32_lob_app_rule_type import Win32LobAppRuleType
from .win32_lob_app_power_shell_script_rule_operation_type import Win32LobAppPowerShellScriptRuleOperationType
from .win32_lob_app_rule_operator import Win32LobAppRuleOperator
from .run_as_account_type import RunAsAccountType

