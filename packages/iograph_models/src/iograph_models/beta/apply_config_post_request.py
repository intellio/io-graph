from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Apply_configPostRequest(BaseModel):
	cloudPcIds: Optional[list[str]] = Field(alias="cloudPcIds", default=None,)
	policySettings: Optional[CloudPcPolicySettingType | str] = Field(alias="policySettings", default=None,)

from .cloud_pc_policy_setting_type import CloudPcPolicySettingType

