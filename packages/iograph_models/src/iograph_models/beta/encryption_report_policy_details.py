from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class EncryptionReportPolicyDetails(BaseModel):
	policyId: Optional[str] = Field(alias="policyId", default=None,)
	policyName: Optional[str] = Field(alias="policyName", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

