from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SharedPCAccountManagerPolicy(BaseModel):
	accountDeletionPolicy: Optional[SharedPCAccountDeletionPolicyType] = Field(default=None,alias="accountDeletionPolicy",)
	cacheAccountsAboveDiskFreePercentage: Optional[int] = Field(default=None,alias="cacheAccountsAboveDiskFreePercentage",)
	inactiveThresholdDays: Optional[int] = Field(default=None,alias="inactiveThresholdDays",)
	removeAccountsBelowDiskFreePercentage: Optional[int] = Field(default=None,alias="removeAccountsBelowDiskFreePercentage",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .shared_p_c_account_deletion_policy_type import SharedPCAccountDeletionPolicyType

