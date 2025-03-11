from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceComplianceScriptRule(BaseModel):
	dataType: Optional[DataType | str] = Field(alias="dataType",default=None,)
	deviceComplianceScriptRuleDataType: Optional[DeviceComplianceScriptRuleDataType | str] = Field(alias="deviceComplianceScriptRuleDataType",default=None,)
	deviceComplianceScriptRulOperator: Optional[DeviceComplianceScriptRulOperator | str] = Field(alias="deviceComplianceScriptRulOperator",default=None,)
	operand: Optional[str] = Field(alias="operand",default=None,)
	operator: Optional[Operator | str] = Field(alias="operator",default=None,)
	settingName: Optional[str] = Field(alias="settingName",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .data_type import DataType
from .device_compliance_script_rule_data_type import DeviceComplianceScriptRuleDataType
from .device_compliance_script_rul_operator import DeviceComplianceScriptRulOperator
from .operator import Operator

