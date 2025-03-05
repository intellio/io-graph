from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AccessPackage(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	isHidden: Optional[bool] = Field(default=None,alias="isHidden",)
	modifiedDateTime: Optional[datetime] = Field(default=None,alias="modifiedDateTime",)
	accessPackagesIncompatibleWith: Optional[list[AccessPackage]] = Field(default=None,alias="accessPackagesIncompatibleWith",)
	assignmentPolicies: Optional[list[AccessPackageAssignmentPolicy]] = Field(default=None,alias="assignmentPolicies",)
	catalog: Optional[AccessPackageCatalog] = Field(default=None,alias="catalog",)
	incompatibleAccessPackages: Optional[list[AccessPackage]] = Field(default=None,alias="incompatibleAccessPackages",)
	incompatibleGroups: Optional[list[Group]] = Field(default=None,alias="incompatibleGroups",)
	resourceRoleScopes: Optional[list[AccessPackageResourceRoleScope]] = Field(default=None,alias="resourceRoleScopes",)

from .access_package_assignment_policy import AccessPackageAssignmentPolicy
from .access_package_catalog import AccessPackageCatalog
from .group import Group
from .access_package_resource_role_scope import AccessPackageResourceRoleScope

