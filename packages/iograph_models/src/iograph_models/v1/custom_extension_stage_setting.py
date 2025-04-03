from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field


class CustomExtensionStageSetting(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.customExtensionStageSetting"] = Field(alias="@odata.type", default="#microsoft.graph.customExtensionStageSetting")
	stage: Optional[AccessPackageCustomExtensionStage | str] = Field(alias="stage", default=None,)
	customExtension: Optional[Union[AccessPackageAssignmentRequestWorkflowExtension, AccessPackageAssignmentWorkflowExtension, OnTokenIssuanceStartCustomExtension, IdentityGovernanceCustomTaskExtension]] = Field(alias="customExtension", default=None,discriminator="odata_type", )

from .access_package_custom_extension_stage import AccessPackageCustomExtensionStage
from .access_package_assignment_request_workflow_extension import AccessPackageAssignmentRequestWorkflowExtension
from .access_package_assignment_workflow_extension import AccessPackageAssignmentWorkflowExtension
from .on_token_issuance_start_custom_extension import OnTokenIssuanceStartCustomExtension
from .identity_governance_custom_task_extension import IdentityGovernanceCustomTaskExtension
