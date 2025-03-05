from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SubjectRightsRequest(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	assignedTo: SerializeAsAny[Optional[Identity]] = Field(alias="assignedTo",default=None,)
	closedDateTime: Optional[datetime] = Field(alias="closedDateTime",default=None,)
	contentQuery: Optional[str] = Field(alias="contentQuery",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	dataSubject: Optional[DataSubject] = Field(alias="dataSubject",default=None,)
	dataSubjectType: Optional[str | DataSubjectType] = Field(alias="dataSubjectType",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	externalId: Optional[str] = Field(alias="externalId",default=None,)
	history: Optional[list[SubjectRightsRequestHistory]] = Field(alias="history",default=None,)
	includeAllVersions: Optional[bool] = Field(alias="includeAllVersions",default=None,)
	includeAuthoredContent: Optional[bool] = Field(alias="includeAuthoredContent",default=None,)
	insight: Optional[SubjectRightsRequestDetail] = Field(alias="insight",default=None,)
	internalDueDateTime: Optional[datetime] = Field(alias="internalDueDateTime",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	mailboxLocations: SerializeAsAny[Optional[SubjectRightsRequestMailboxLocation]] = Field(alias="mailboxLocations",default=None,)
	pauseAfterEstimate: Optional[bool] = Field(alias="pauseAfterEstimate",default=None,)
	regulations: Optional[list[str]] = Field(alias="regulations",default=None,)
	siteLocations: SerializeAsAny[Optional[SubjectRightsRequestSiteLocation]] = Field(alias="siteLocations",default=None,)
	stages: Optional[list[SubjectRightsRequestStageDetail]] = Field(alias="stages",default=None,)
	status: Optional[str | SubjectRightsRequestStatus] = Field(alias="status",default=None,)
	type: Optional[str | SubjectRightsRequestType] = Field(alias="type",default=None,)
	approvers: Optional[list[User]] = Field(alias="approvers",default=None,)
	collaborators: Optional[list[User]] = Field(alias="collaborators",default=None,)
	notes: Optional[list[AuthoredNote]] = Field(alias="notes",default=None,)
	team: Optional[Team] = Field(alias="team",default=None,)

from .identity import Identity
from .identity_set import IdentitySet
from .data_subject import DataSubject
from .data_subject_type import DataSubjectType
from .subject_rights_request_history import SubjectRightsRequestHistory
from .subject_rights_request_detail import SubjectRightsRequestDetail
from .identity_set import IdentitySet
from .subject_rights_request_mailbox_location import SubjectRightsRequestMailboxLocation
from .subject_rights_request_site_location import SubjectRightsRequestSiteLocation
from .subject_rights_request_stage_detail import SubjectRightsRequestStageDetail
from .subject_rights_request_status import SubjectRightsRequestStatus
from .subject_rights_request_type import SubjectRightsRequestType
from .user import User
from .user import User
from .authored_note import AuthoredNote
from .team import Team

