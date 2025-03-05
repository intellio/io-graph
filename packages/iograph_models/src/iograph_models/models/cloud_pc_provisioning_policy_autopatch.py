from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcProvisioningPolicyAutopatch(BaseModel):
	autopatchGroupId: Optional[str] = Field(default=None,alias="autopatchGroupId",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


