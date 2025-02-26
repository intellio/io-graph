from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class AccessPackageResourceRequest(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	requestType: Optional[AccessPackageRequestType] = Field(default=None,alias="requestType",)
	state: Optional[AccessPackageRequestState] = Field(default=None,alias="state",)
	catalog: Optional[AccessPackageCatalog] = Field(default=None,alias="catalog",)
	resource: Optional[AccessPackageResource] = Field(default=None,alias="resource",)

from .access_package_request_type import AccessPackageRequestType
from .access_package_request_state import AccessPackageRequestState
from .access_package_catalog import AccessPackageCatalog
from .access_package_resource import AccessPackageResource

