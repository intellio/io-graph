from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EntitlementManagement(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	accessPackageAssignmentApprovals: Optional[list[Approval]] = Field(alias="accessPackageAssignmentApprovals", default=None,)
	accessPackageAssignmentPolicies: Optional[list[AccessPackageAssignmentPolicy]] = Field(alias="accessPackageAssignmentPolicies", default=None,)
	accessPackageAssignmentRequests: Optional[list[AccessPackageAssignmentRequest]] = Field(alias="accessPackageAssignmentRequests", default=None,)
	accessPackageAssignmentResourceRoles: Optional[list[AccessPackageAssignmentResourceRole]] = Field(alias="accessPackageAssignmentResourceRoles", default=None,)
	accessPackageAssignments: Optional[list[AccessPackageAssignment]] = Field(alias="accessPackageAssignments", default=None,)
	accessPackageCatalogs: Optional[list[AccessPackageCatalog]] = Field(alias="accessPackageCatalogs", default=None,)
	accessPackageResourceEnvironments: Optional[list[AccessPackageResourceEnvironment]] = Field(alias="accessPackageResourceEnvironments", default=None,)
	accessPackageResourceRequests: Optional[list[AccessPackageResourceRequest]] = Field(alias="accessPackageResourceRequests", default=None,)
	accessPackageResourceRoleScopes: Optional[list[AccessPackageResourceRoleScope]] = Field(alias="accessPackageResourceRoleScopes", default=None,)
	accessPackageResources: Optional[list[AccessPackageResource]] = Field(alias="accessPackageResources", default=None,)
	accessPackages: Optional[list[AccessPackage]] = Field(alias="accessPackages", default=None,)
	assignmentRequests: Optional[list[AccessPackageAssignmentRequest]] = Field(alias="assignmentRequests", default=None,)
	connectedOrganizations: Optional[list[ConnectedOrganization]] = Field(alias="connectedOrganizations", default=None,)
	settings: Optional[EntitlementManagementSettings] = Field(alias="settings", default=None,)
	subjects: Optional[list[AccessPackageSubject]] = Field(alias="subjects", default=None,)

from .approval import Approval
from .access_package_assignment_policy import AccessPackageAssignmentPolicy
from .access_package_assignment_request import AccessPackageAssignmentRequest
from .access_package_assignment_resource_role import AccessPackageAssignmentResourceRole
from .access_package_assignment import AccessPackageAssignment
from .access_package_catalog import AccessPackageCatalog
from .access_package_resource_environment import AccessPackageResourceEnvironment
from .access_package_resource_request import AccessPackageResourceRequest
from .access_package_resource_role_scope import AccessPackageResourceRoleScope
from .access_package_resource import AccessPackageResource
from .access_package import AccessPackage
from .access_package_assignment_request import AccessPackageAssignmentRequest
from .connected_organization import ConnectedOrganization
from .entitlement_management_settings import EntitlementManagementSettings
from .access_package_subject import AccessPackageSubject

