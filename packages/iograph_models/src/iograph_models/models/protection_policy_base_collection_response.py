from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ProtectionPolicyBaseCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[ProtectionPolicyBase] = Field(alias="value",)

from .protection_policy_base import ProtectionPolicyBase

