from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class EntitlementManagement(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	accessPackageAssignmentApprovals: list[Approval] = Field(alias="accessPackageAssignmentApprovals",)
	accessPackages: list[AccessPackage] = Field(alias="accessPackages",)
	assignmentPolicies: list[AccessPackageAssignmentPolicy] = Field(alias="assignmentPolicies",)
	assignmentRequests: list[AccessPackageAssignmentRequest] = Field(alias="assignmentRequests",)
	assignments: list[AccessPackageAssignment] = Field(alias="assignments",)
	catalogs: list[AccessPackageCatalog] = Field(alias="catalogs",)
	connectedOrganizations: list[ConnectedOrganization] = Field(alias="connectedOrganizations",)
	resourceEnvironments: list[AccessPackageResourceEnvironment] = Field(alias="resourceEnvironments",)
	resourceRequests: list[AccessPackageResourceRequest] = Field(alias="resourceRequests",)
	resourceRoleScopes: list[AccessPackageResourceRoleScope] = Field(alias="resourceRoleScopes",)
	resources: list[AccessPackageResource] = Field(alias="resources",)
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

