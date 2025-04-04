from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class AccessPackageResourceRequest(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.accessPackageResourceRequest"] = Field(alias="@odata.type", default="#microsoft.graph.accessPackageResourceRequest")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	requestType: Optional[AccessPackageRequestType | str] = Field(alias="requestType", default=None,)
	state: Optional[AccessPackageRequestState | str] = Field(alias="state", default=None,)
	catalog: Optional[AccessPackageCatalog] = Field(alias="catalog", default=None,)
	resource: Optional[AccessPackageResource] = Field(alias="resource", default=None,)

from .access_package_request_type import AccessPackageRequestType
from .access_package_request_state import AccessPackageRequestState
from .access_package_catalog import AccessPackageCatalog
from .access_package_resource import AccessPackageResource
