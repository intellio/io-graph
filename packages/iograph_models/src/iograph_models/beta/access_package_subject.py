from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class AccessPackageSubject(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.accessPackageSubject"] = Field(alias="@odata.type",)
	altSecId: Optional[str] = Field(alias="altSecId", default=None,)
	cleanupScheduledDateTime: Optional[datetime] = Field(alias="cleanupScheduledDateTime", default=None,)
	connectedOrganizationId: Optional[str] = Field(alias="connectedOrganizationId", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	email: Optional[str] = Field(alias="email", default=None,)
	objectId: Optional[str] = Field(alias="objectId", default=None,)
	onPremisesSecurityIdentifier: Optional[str] = Field(alias="onPremisesSecurityIdentifier", default=None,)
	principalName: Optional[str] = Field(alias="principalName", default=None,)
	subjectLifecycle: Optional[AccessPackageSubjectLifecycle | str] = Field(alias="subjectLifecycle", default=None,)
	type: Optional[str] = Field(alias="type", default=None,)
	connectedOrganization: Optional[ConnectedOrganization] = Field(alias="connectedOrganization", default=None,)

from .access_package_subject_lifecycle import AccessPackageSubjectLifecycle
from .connected_organization import ConnectedOrganization
