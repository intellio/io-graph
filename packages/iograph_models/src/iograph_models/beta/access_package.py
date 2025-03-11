from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AccessPackage(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	catalogId: Optional[str] = Field(alias="catalogId",default=None,)
	createdBy: Optional[str] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	isHidden: Optional[bool] = Field(alias="isHidden",default=None,)
	isRoleScopesVisible: Optional[bool] = Field(alias="isRoleScopesVisible",default=None,)
	modifiedBy: Optional[str] = Field(alias="modifiedBy",default=None,)
	modifiedDateTime: Optional[datetime] = Field(alias="modifiedDateTime",default=None,)
	uniqueName: Optional[str] = Field(alias="uniqueName",default=None,)
	accessPackageAssignmentPolicies: Optional[list[AccessPackageAssignmentPolicy]] = Field(alias="accessPackageAssignmentPolicies",default=None,)
	accessPackageCatalog: Optional[AccessPackageCatalog] = Field(alias="accessPackageCatalog",default=None,)
	accessPackageResourceRoleScopes: Optional[list[AccessPackageResourceRoleScope]] = Field(alias="accessPackageResourceRoleScopes",default=None,)
	accessPackagesIncompatibleWith: Optional[list[AccessPackage]] = Field(alias="accessPackagesIncompatibleWith",default=None,)
	incompatibleAccessPackages: Optional[list[AccessPackage]] = Field(alias="incompatibleAccessPackages",default=None,)
	incompatibleGroups: Optional[list[Group]] = Field(alias="incompatibleGroups",default=None,)

from .access_package_assignment_policy import AccessPackageAssignmentPolicy
from .access_package_catalog import AccessPackageCatalog
from .access_package_resource_role_scope import AccessPackageResourceRoleScope
from .group import Group

