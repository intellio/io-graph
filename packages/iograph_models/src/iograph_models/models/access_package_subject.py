from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AccessPackageSubject(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	email: Optional[str] = Field(default=None,alias="email",)
	objectId: Optional[str] = Field(default=None,alias="objectId",)
	onPremisesSecurityIdentifier: Optional[str] = Field(default=None,alias="onPremisesSecurityIdentifier",)
	principalName: Optional[str] = Field(default=None,alias="principalName",)
	subjectType: Optional[AccessPackageSubjectType] = Field(default=None,alias="subjectType",)
	connectedOrganization: Optional[ConnectedOrganization] = Field(default=None,alias="connectedOrganization",)

from .access_package_subject_type import AccessPackageSubjectType
from .connected_organization import ConnectedOrganization

