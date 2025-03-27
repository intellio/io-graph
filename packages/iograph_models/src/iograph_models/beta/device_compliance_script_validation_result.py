from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceComplianceScriptValidationResult(BaseModel):
	ruleErrors: Optional[list[DeviceComplianceScriptRuleError]] = Field(alias="ruleErrors", default=None,)
	rules: Optional[list[DeviceComplianceScriptRule]] = Field(alias="rules", default=None,)
	scriptErrors: Optional[list[Annotated[Union[DeviceComplianceScriptRuleError]],Field(discriminator="odata_type")]]] = Field(alias="scriptErrors", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .device_compliance_script_rule_error import DeviceComplianceScriptRuleError
from .device_compliance_script_rule import DeviceComplianceScriptRule
from .device_compliance_script_rule_error import DeviceComplianceScriptRuleError

