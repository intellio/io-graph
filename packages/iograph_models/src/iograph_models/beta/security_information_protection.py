from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class SecurityInformationProtection(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.security.informationProtection"] = Field(alias="@odata.type",)
	labelPolicySettings: Optional[SecurityInformationProtectionPolicySetting] = Field(alias="labelPolicySettings", default=None,)
	sensitivityLabels: Optional[list[SecuritySensitivityLabel]] = Field(alias="sensitivityLabels", default=None,)

from .security_information_protection_policy_setting import SecurityInformationProtectionPolicySetting
from .security_sensitivity_label import SecuritySensitivityLabel
