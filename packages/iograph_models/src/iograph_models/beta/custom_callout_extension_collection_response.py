from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class CustomCalloutExtensionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[AccessPackageAssignmentRequestWorkflowExtension, AccessPackageAssignmentWorkflowExtension, CustomAccessPackageWorkflowExtension, CustomAuthenticationExtension, OnAttributeCollectionStartCustomExtension, OnAttributeCollectionSubmitCustomExtension, OnOtpSendCustomExtension, OnTokenIssuanceStartCustomExtension, IdentityGovernanceCustomTaskExtension],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .access_package_assignment_request_workflow_extension import AccessPackageAssignmentRequestWorkflowExtension
from .access_package_assignment_workflow_extension import AccessPackageAssignmentWorkflowExtension
from .custom_access_package_workflow_extension import CustomAccessPackageWorkflowExtension
from .custom_authentication_extension import CustomAuthenticationExtension
from .on_attribute_collection_start_custom_extension import OnAttributeCollectionStartCustomExtension
from .on_attribute_collection_submit_custom_extension import OnAttributeCollectionSubmitCustomExtension
from .on_otp_send_custom_extension import OnOtpSendCustomExtension
from .on_token_issuance_start_custom_extension import OnTokenIssuanceStartCustomExtension
from .identity_governance_custom_task_extension import IdentityGovernanceCustomTaskExtension

