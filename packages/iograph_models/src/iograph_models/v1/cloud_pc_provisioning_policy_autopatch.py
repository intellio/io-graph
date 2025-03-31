from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CloudPcProvisioningPolicyAutopatch(BaseModel):
	autopatchGroupId: Optional[str] = Field(alias="autopatchGroupId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

