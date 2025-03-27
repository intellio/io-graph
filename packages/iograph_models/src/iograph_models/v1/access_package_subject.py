from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AccessPackageSubject(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	email: Optional[str] = Field(alias="email", default=None,)
	objectId: Optional[str] = Field(alias="objectId", default=None,)
	onPremisesSecurityIdentifier: Optional[str] = Field(alias="onPremisesSecurityIdentifier", default=None,)
	principalName: Optional[str] = Field(alias="principalName", default=None,)
	subjectType: Optional[AccessPackageSubjectType | str] = Field(alias="subjectType", default=None,)
	connectedOrganization: Optional[ConnectedOrganization] = Field(alias="connectedOrganization", default=None,)

from .access_package_subject_type import AccessPackageSubjectType
from .connected_organization import ConnectedOrganization

