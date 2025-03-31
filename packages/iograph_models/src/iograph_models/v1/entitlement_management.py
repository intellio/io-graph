from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class EntitlementManagement(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.entitlementManagement"] = Field(alias="@odata.type",)
	accessPackageAssignmentApprovals: Optional[list[Approval]] = Field(alias="accessPackageAssignmentApprovals", default=None,)
	accessPackages: Optional[list[AccessPackage]] = Field(alias="accessPackages", default=None,)
	assignmentPolicies: Optional[list[AccessPackageAssignmentPolicy]] = Field(alias="assignmentPolicies", default=None,)
	assignmentRequests: Optional[list[AccessPackageAssignmentRequest]] = Field(alias="assignmentRequests", default=None,)
	assignments: Optional[list[AccessPackageAssignment]] = Field(alias="assignments", default=None,)
	catalogs: Optional[list[AccessPackageCatalog]] = Field(alias="catalogs", default=None,)
	connectedOrganizations: Optional[list[ConnectedOrganization]] = Field(alias="connectedOrganizations", default=None,)
	resourceEnvironments: Optional[list[AccessPackageResourceEnvironment]] = Field(alias="resourceEnvironments", default=None,)
	resourceRequests: Optional[list[AccessPackageResourceRequest]] = Field(alias="resourceRequests", default=None,)
	resourceRoleScopes: Optional[list[AccessPackageResourceRoleScope]] = Field(alias="resourceRoleScopes", default=None,)
	resources: Optional[list[AccessPackageResource]] = Field(alias="resources", default=None,)
	settings: Optional[EntitlementManagementSettings] = Field(alias="settings", default=None,)

from .approval import Approval
from .access_package import AccessPackage
from .access_package_assignment_policy import AccessPackageAssignmentPolicy
from .access_package_assignment_request import AccessPackageAssignmentRequest
from .access_package_assignment import AccessPackageAssignment
from .access_package_catalog import AccessPackageCatalog
from .connected_organization import ConnectedOrganization
from .access_package_resource_environment import AccessPackageResourceEnvironment
from .access_package_resource_request import AccessPackageResourceRequest
from .access_package_resource_role_scope import AccessPackageResourceRoleScope
from .access_package_resource import AccessPackageResource
from .entitlement_management_settings import EntitlementManagementSettings
