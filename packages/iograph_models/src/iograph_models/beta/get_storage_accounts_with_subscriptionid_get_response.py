from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Get_storage_accounts_with_subscriptionidGetResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[CloudPcForensicStorageAccount]] = Field(alias="value", default=None,)

from .cloud_pc_forensic_storage_account import CloudPcForensicStorageAccount
