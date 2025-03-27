from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class Win32LobAppPowerShellScriptRequirement(BaseModel):
	detectionValue: Optional[str] = Field(alias="detectionValue", default=None,)
	operator: Optional[Win32LobAppDetectionOperator | str] = Field(alias="operator", default=None,)
	odata_type: Literal["#microsoft.graph.win32LobAppPowerShellScriptRequirement"] = Field(alias="@odata.type", default="#microsoft.graph.win32LobAppPowerShellScriptRequirement")
	detectionType: Optional[Win32LobAppPowerShellScriptDetectionType | str] = Field(alias="detectionType", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	enforceSignatureCheck: Optional[bool] = Field(alias="enforceSignatureCheck", default=None,)
	runAs32Bit: Optional[bool] = Field(alias="runAs32Bit", default=None,)
	runAsAccount: Optional[RunAsAccountType | str] = Field(alias="runAsAccount", default=None,)
	scriptContent: Optional[str] = Field(alias="scriptContent", default=None,)

from .win32_lob_app_detection_operator import Win32LobAppDetectionOperator
from .win32_lob_app_power_shell_script_detection_type import Win32LobAppPowerShellScriptDetectionType
from .run_as_account_type import RunAsAccountType

