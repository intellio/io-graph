from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AccessPackageCatalog(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	catalogType: Optional[AccessPackageCatalogType | str] = Field(alias="catalogType", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	isExternallyVisible: Optional[bool] = Field(alias="isExternallyVisible", default=None,)
	modifiedDateTime: Optional[datetime] = Field(alias="modifiedDateTime", default=None,)
	state: Optional[AccessPackageCatalogState | str] = Field(alias="state", default=None,)
	accessPackages: Optional[list[AccessPackage]] = Field(alias="accessPackages", default=None,)
	customWorkflowExtensions: Optional[list[Annotated[Union[AccessPackageAssignmentRequestWorkflowExtension, AccessPackageAssignmentWorkflowExtension, CustomAuthenticationExtension, OnTokenIssuanceStartCustomExtension, IdentityGovernanceCustomTaskExtension]],Field(discriminator="odata_type")]]] = Field(alias="customWorkflowExtensions", default=None,)
	resourceRoles: Optional[list[AccessPackageResourceRole]] = Field(alias="resourceRoles", default=None,)
	resources: Optional[list[AccessPackageResource]] = Field(alias="resources", default=None,)
	resourceScopes: Optional[list[AccessPackageResourceScope]] = Field(alias="resourceScopes", default=None,)

from .access_package_catalog_type import AccessPackageCatalogType
from .access_package_catalog_state import AccessPackageCatalogState
from .access_package import AccessPackage
from .access_package_assignment_request_workflow_extension import AccessPackageAssignmentRequestWorkflowExtension
from .access_package_assignment_workflow_extension import AccessPackageAssignmentWorkflowExtension
from .custom_authentication_extension import CustomAuthenticationExtension
from .on_token_issuance_start_custom_extension import OnTokenIssuanceStartCustomExtension
from .identity_governance_custom_task_extension import IdentityGovernanceCustomTaskExtension
from .access_package_resource_role import AccessPackageResourceRole
from .access_package_resource import AccessPackageResource
from .access_package_resource_scope import AccessPackageResourceScope

