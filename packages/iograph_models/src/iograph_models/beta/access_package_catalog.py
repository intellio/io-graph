from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AccessPackageCatalog(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	catalogStatus: Optional[str] = Field(alias="catalogStatus",default=None,)
	catalogType: Optional[str] = Field(alias="catalogType",default=None,)
	createdBy: Optional[str] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	isExternallyVisible: Optional[bool] = Field(alias="isExternallyVisible",default=None,)
	modifiedBy: Optional[str] = Field(alias="modifiedBy",default=None,)
	modifiedDateTime: Optional[datetime] = Field(alias="modifiedDateTime",default=None,)
	uniqueName: Optional[str] = Field(alias="uniqueName",default=None,)
	accessPackageCustomWorkflowExtensions: SerializeAsAny[Optional[list[CustomCalloutExtension]]] = Field(alias="accessPackageCustomWorkflowExtensions",default=None,)
	accessPackageResourceRoles: Optional[list[AccessPackageResourceRole]] = Field(alias="accessPackageResourceRoles",default=None,)
	accessPackageResources: Optional[list[AccessPackageResource]] = Field(alias="accessPackageResources",default=None,)
	accessPackageResourceScopes: Optional[list[AccessPackageResourceScope]] = Field(alias="accessPackageResourceScopes",default=None,)
	accessPackages: Optional[list[AccessPackage]] = Field(alias="accessPackages",default=None,)
	customAccessPackageWorkflowExtensions: Optional[list[CustomAccessPackageWorkflowExtension]] = Field(alias="customAccessPackageWorkflowExtensions",default=None,)

from .custom_callout_extension import CustomCalloutExtension
from .access_package_resource_role import AccessPackageResourceRole
from .access_package_resource import AccessPackageResource
from .access_package_resource_scope import AccessPackageResourceScope
from .access_package import AccessPackage
from .custom_access_package_workflow_extension import CustomAccessPackageWorkflowExtension

