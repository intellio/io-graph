from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AccessPackageCatalog(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	catalogType: Optional[str | AccessPackageCatalogType] = Field(alias="catalogType",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	isExternallyVisible: Optional[bool] = Field(alias="isExternallyVisible",default=None,)
	modifiedDateTime: Optional[datetime] = Field(alias="modifiedDateTime",default=None,)
	state: Optional[str | AccessPackageCatalogState] = Field(alias="state",default=None,)
	accessPackages: Optional[list[AccessPackage]] = Field(alias="accessPackages",default=None,)
	customWorkflowExtensions: SerializeAsAny[Optional[list[CustomCalloutExtension]]] = Field(alias="customWorkflowExtensions",default=None,)
	resourceRoles: Optional[list[AccessPackageResourceRole]] = Field(alias="resourceRoles",default=None,)
	resources: Optional[list[AccessPackageResource]] = Field(alias="resources",default=None,)
	resourceScopes: Optional[list[AccessPackageResourceScope]] = Field(alias="resourceScopes",default=None,)

from .access_package_catalog_type import AccessPackageCatalogType
from .access_package_catalog_state import AccessPackageCatalogState
from .access_package import AccessPackage
from .custom_callout_extension import CustomCalloutExtension
from .access_package_resource_role import AccessPackageResourceRole
from .access_package_resource import AccessPackageResource
from .access_package_resource_scope import AccessPackageResourceScope

