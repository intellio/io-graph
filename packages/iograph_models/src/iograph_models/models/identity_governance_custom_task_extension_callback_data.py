from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IdentityGovernanceCustomTaskExtensionCallbackData(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	operationStatus: Optional[IdentityGovernanceCustomTaskExtensionOperationStatus] = Field(default=None,alias="operationStatus",)

from .identity_governance_custom_task_extension_operation_status import IdentityGovernanceCustomTaskExtensionOperationStatus

