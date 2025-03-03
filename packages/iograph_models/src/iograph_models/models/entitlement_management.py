from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class EntitlementManagement(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	accessPackageAssignmentApprovals: Optional[list[Approval]] = Field(default=None,alias="accessPackageAssignmentApprovals",)
	accessPackages: Optional[list[AccessPackage]] = Field(default=None,alias="accessPackages",)
	assignmentPolicies: Optional[list[AccessPackageAssignmentPolicy]] = Field(default=None,alias="assignmentPolicies",)
	assignmentRequests: Optional[list[AccessPackageAssignmentRequest]] = Field(default=None,alias="assignmentRequests",)
	assignments: Optional[list[AccessPackageAssignment]] = Field(default=None,alias="assignments",)
	catalogs: Optional[list[AccessPackageCatalog]] = Field(default=None,alias="catalogs",)
	connectedOrganizations: Optional[list[ConnectedOrganization]] = Field(default=None,alias="connectedOrganizations",)
	resourceEnvironments: Optional[list[AccessPackageResourceEnvironment]] = Field(default=None,alias="resourceEnvironments",)
	resourceRequests: Optional[list[AccessPackageResourceRequest]] = Field(default=None,alias="resourceRequests",)
	resourceRoleScopes: Optional[list[AccessPackageResourceRoleScope]] = Field(default=None,alias="resourceRoleScopes",)
	resources: Optional[list[AccessPackageResource]] = Field(default=None,alias="resources",)
	settings: Optional[EntitlementManagementSettings] = Field(default=None,alias="settings",)

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

