from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DeviceComplianceScriptRuleError(BaseModel):
	code: Optional[Code | str] = Field(alias="code", default=None,)
	deviceComplianceScriptRulesValidationError: Optional[DeviceComplianceScriptRulesValidationError | str] = Field(alias="deviceComplianceScriptRulesValidationError", default=None,)
	message: Optional[str] = Field(alias="message", default=None,)
	odata_type: Literal["#microsoft.graph.deviceComplianceScriptRuleError"] = Field(alias="@odata.type", default="#microsoft.graph.deviceComplianceScriptRuleError")
	settingName: Optional[str] = Field(alias="settingName", default=None,)

from .code import Code
from .device_compliance_script_rules_validation_error import DeviceComplianceScriptRulesValidationError
