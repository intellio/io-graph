from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityGovernanceCustomTaskExtensionCallbackData(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	operationStatus: Optional[str | IdentityGovernanceCustomTaskExtensionOperationStatus] = Field(alias="operationStatus",default=None,)

from .identity_governance_custom_task_extension_operation_status import IdentityGovernanceCustomTaskExtensionOperationStatus

