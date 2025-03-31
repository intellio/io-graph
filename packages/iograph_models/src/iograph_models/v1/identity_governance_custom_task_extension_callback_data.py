from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class IdentityGovernanceCustomTaskExtensionCallbackData(BaseModel):
	odata_type: Literal["#microsoft.graph.identityGovernance.customTaskExtensionCallbackData"] = Field(alias="@odata.type", default="#microsoft.graph.identityGovernance.customTaskExtensionCallbackData")
	operationStatus: Optional[IdentityGovernanceCustomTaskExtensionOperationStatus | str] = Field(alias="operationStatus", default=None,)

from .identity_governance_custom_task_extension_operation_status import IdentityGovernanceCustomTaskExtensionOperationStatus
