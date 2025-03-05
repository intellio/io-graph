from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AccessPackageResourceRequest(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	requestType: Optional[str | AccessPackageRequestType] = Field(alias="requestType",default=None,)
	state: Optional[str | AccessPackageRequestState] = Field(alias="state",default=None,)
	catalog: Optional[AccessPackageCatalog] = Field(alias="catalog",default=None,)
	resource: Optional[AccessPackageResource] = Field(alias="resource",default=None,)

from .access_package_request_type import AccessPackageRequestType
from .access_package_request_state import AccessPackageRequestState
from .access_package_catalog import AccessPackageCatalog
from .access_package_resource import AccessPackageResource

