from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field


class ResumePostRequest(BaseModel):
	source: Optional[str] = Field(alias="source", default=None,)
	type: Optional[str] = Field(alias="type", default=None,)
	data: Optional[Union[AccessPackageAssignmentRequestCallbackData, IdentityGovernanceCustomTaskExtensionCallbackData, IdentityGovernanceCustomTaskExtensionCalloutData]] = Field(alias="data", default=None,discriminator="odata_type", )

from .access_package_assignment_request_callback_data import AccessPackageAssignmentRequestCallbackData
from .identity_governance_custom_task_extension_callback_data import IdentityGovernanceCustomTaskExtensionCallbackData
from .identity_governance_custom_task_extension_callout_data import IdentityGovernanceCustomTaskExtensionCalloutData
