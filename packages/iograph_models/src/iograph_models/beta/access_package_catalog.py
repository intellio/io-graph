from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AccessPackageCatalog(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	catalogStatus: Optional[str] = Field(alias="catalogStatus", default=None,)
	catalogType: Optional[str] = Field(alias="catalogType", default=None,)
	createdBy: Optional[str] = Field(alias="createdBy", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	isExternallyVisible: Optional[bool] = Field(alias="isExternallyVisible", default=None,)
	modifiedBy: Optional[str] = Field(alias="modifiedBy", default=None,)
	modifiedDateTime: Optional[datetime] = Field(alias="modifiedDateTime", default=None,)
	uniqueName: Optional[str] = Field(alias="uniqueName", default=None,)
	accessPackageCustomWorkflowExtensions: Optional[list[Annotated[Union[AccessPackageAssignmentRequestWorkflowExtension, AccessPackageAssignmentWorkflowExtension, CustomAccessPackageWorkflowExtension, CustomAuthenticationExtension, OnAttributeCollectionStartCustomExtension, OnAttributeCollectionSubmitCustomExtension, OnOtpSendCustomExtension, OnTokenIssuanceStartCustomExtension, IdentityGovernanceCustomTaskExtension]],Field(discriminator="odata_type")]]] = Field(alias="accessPackageCustomWorkflowExtensions", default=None,)
	accessPackageResourceRoles: Optional[list[AccessPackageResourceRole]] = Field(alias="accessPackageResourceRoles", default=None,)
	accessPackageResources: Optional[list[AccessPackageResource]] = Field(alias="accessPackageResources", default=None,)
	accessPackageResourceScopes: Optional[list[AccessPackageResourceScope]] = Field(alias="accessPackageResourceScopes", default=None,)
	accessPackages: Optional[list[AccessPackage]] = Field(alias="accessPackages", default=None,)
	customAccessPackageWorkflowExtensions: Optional[list[CustomAccessPackageWorkflowExtension]] = Field(alias="customAccessPackageWorkflowExtensions", default=None,)

from .access_package_assignment_request_workflow_extension import AccessPackageAssignmentRequestWorkflowExtension
from .access_package_assignment_workflow_extension import AccessPackageAssignmentWorkflowExtension
from .custom_access_package_workflow_extension import CustomAccessPackageWorkflowExtension
from .custom_authentication_extension import CustomAuthenticationExtension
from .on_attribute_collection_start_custom_extension import OnAttributeCollectionStartCustomExtension
from .on_attribute_collection_submit_custom_extension import OnAttributeCollectionSubmitCustomExtension
from .on_otp_send_custom_extension import OnOtpSendCustomExtension
from .on_token_issuance_start_custom_extension import OnTokenIssuanceStartCustomExtension
from .identity_governance_custom_task_extension import IdentityGovernanceCustomTaskExtension
from .access_package_resource_role import AccessPackageResourceRole
from .access_package_resource import AccessPackageResource
from .access_package_resource_scope import AccessPackageResourceScope
from .access_package import AccessPackage
from .custom_access_package_workflow_extension import CustomAccessPackageWorkflowExtension

