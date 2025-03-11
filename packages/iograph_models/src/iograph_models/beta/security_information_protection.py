from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityInformationProtection(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	labelPolicySettings: Optional[SecurityInformationProtectionPolicySetting] = Field(alias="labelPolicySettings",default=None,)
	sensitivityLabels: Optional[list[SecuritySensitivityLabel]] = Field(alias="sensitivityLabels",default=None,)

from .security_information_protection_policy_setting import SecurityInformationProtectionPolicySetting
from .security_sensitivity_label import SecuritySensitivityLabel

