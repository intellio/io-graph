from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AccessPackage(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	isHidden: Optional[bool] = Field(alias="isHidden", default=None,)
	modifiedDateTime: Optional[datetime] = Field(alias="modifiedDateTime", default=None,)
	accessPackagesIncompatibleWith: Optional[list[AccessPackage]] = Field(alias="accessPackagesIncompatibleWith", default=None,)
	assignmentPolicies: Optional[list[AccessPackageAssignmentPolicy]] = Field(alias="assignmentPolicies", default=None,)
	catalog: Optional[AccessPackageCatalog] = Field(alias="catalog", default=None,)
	incompatibleAccessPackages: Optional[list[AccessPackage]] = Field(alias="incompatibleAccessPackages", default=None,)
	incompatibleGroups: Optional[list[Group]] = Field(alias="incompatibleGroups", default=None,)
	resourceRoleScopes: Optional[list[AccessPackageResourceRoleScope]] = Field(alias="resourceRoleScopes", default=None,)

from .access_package_assignment_policy import AccessPackageAssignmentPolicy
from .access_package_catalog import AccessPackageCatalog
from .group import Group
from .access_package_resource_role_scope import AccessPackageResourceRoleScope

