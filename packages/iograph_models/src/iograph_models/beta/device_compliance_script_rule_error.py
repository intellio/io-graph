from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceComplianceScriptRuleError(BaseModel):
	code: Optional[Code | str] = Field(alias="code",default=None,)
	deviceComplianceScriptRulesValidationError: Optional[DeviceComplianceScriptRulesValidationError | str] = Field(alias="deviceComplianceScriptRulesValidationError",default=None,)
	message: Optional[str] = Field(alias="message",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	settingName: Optional[str] = Field(alias="settingName",default=None,)

from .code import Code
from .device_compliance_script_rules_validation_error import DeviceComplianceScriptRulesValidationError

