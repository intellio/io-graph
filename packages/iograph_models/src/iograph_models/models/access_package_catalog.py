from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class AccessPackageCatalog(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	catalogType: Optional[AccessPackageCatalogType] = Field(default=None,alias="catalogType",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	isExternallyVisible: Optional[bool] = Field(default=None,alias="isExternallyVisible",)
	modifiedDateTime: Optional[datetime] = Field(default=None,alias="modifiedDateTime",)
	state: Optional[AccessPackageCatalogState] = Field(default=None,alias="state",)
	accessPackages: list[AccessPackage] = Field(alias="accessPackages",)
	customWorkflowExtensions: list[CustomCalloutExtension] = Field(alias="customWorkflowExtensions",)
	resourceRoles: list[AccessPackageResourceRole] = Field(alias="resourceRoles",)
	resources: list[AccessPackageResource] = Field(alias="resources",)
	resourceScopes: list[AccessPackageResourceScope] = Field(alias="resourceScopes",)

from .access_package_catalog_type import AccessPackageCatalogType
from .access_package_catalog_state import AccessPackageCatalogState
from .access_package import AccessPackage
from .custom_callout_extension import CustomCalloutExtension
from .access_package_resource_role import AccessPackageResourceRole
from .access_package_resource import AccessPackageResource
from .access_package_resource_scope import AccessPackageResourceScope

