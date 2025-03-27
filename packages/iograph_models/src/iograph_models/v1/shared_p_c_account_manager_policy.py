from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SharedPCAccountManagerPolicy(BaseModel):
	accountDeletionPolicy: Optional[SharedPCAccountDeletionPolicyType | str] = Field(alias="accountDeletionPolicy", default=None,)
	cacheAccountsAboveDiskFreePercentage: Optional[int] = Field(alias="cacheAccountsAboveDiskFreePercentage", default=None,)
	inactiveThresholdDays: Optional[int] = Field(alias="inactiveThresholdDays", default=None,)
	removeAccountsBelowDiskFreePercentage: Optional[int] = Field(alias="removeAccountsBelowDiskFreePercentage", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .shared_p_c_account_deletion_policy_type import SharedPCAccountDeletionPolicyType

