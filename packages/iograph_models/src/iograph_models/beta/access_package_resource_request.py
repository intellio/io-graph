from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class AccessPackageResourceRequest(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.accessPackageResourceRequest"] = Field(alias="@odata.type",)
	catalogId: Optional[str] = Field(alias="catalogId", default=None,)
	executeImmediately: Optional[bool] = Field(alias="executeImmediately", default=None,)
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime", default=None,)
	isValidationOnly: Optional[bool] = Field(alias="isValidationOnly", default=None,)
	justification: Optional[str] = Field(alias="justification", default=None,)
	requestState: Optional[str] = Field(alias="requestState", default=None,)
	requestStatus: Optional[str] = Field(alias="requestStatus", default=None,)
	requestType: Optional[str] = Field(alias="requestType", default=None,)
	accessPackageResource: Optional[AccessPackageResource] = Field(alias="accessPackageResource", default=None,)
	requestor: Optional[AccessPackageSubject] = Field(alias="requestor", default=None,)

from .access_package_resource import AccessPackageResource
from .access_package_subject import AccessPackageSubject
