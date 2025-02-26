from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class AccessPackage(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	isHidden: Optional[bool] = Field(default=None,alias="isHidden",)
	modifiedDateTime: Optional[datetime] = Field(default=None,alias="modifiedDateTime",)
	accessPackagesIncompatibleWith: list[AccessPackage] = Field(alias="accessPackagesIncompatibleWith",)
	assignmentPolicies: list[AccessPackageAssignmentPolicy] = Field(alias="assignmentPolicies",)
	catalog: Optional[AccessPackageCatalog] = Field(default=None,alias="catalog",)
	incompatibleAccessPackages: list[AccessPackage] = Field(alias="incompatibleAccessPackages",)
	incompatibleGroups: list[Group] = Field(alias="incompatibleGroups",)
	resourceRoleScopes: list[AccessPackageResourceRoleScope] = Field(alias="resourceRoleScopes",)

from .access_package_assignment_policy import AccessPackageAssignmentPolicy
from .access_package_catalog import AccessPackageCatalog
from .group import Group
from .access_package_resource_role_scope import AccessPackageResourceRoleScope

