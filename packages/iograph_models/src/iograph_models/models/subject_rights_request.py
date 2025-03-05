from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SubjectRightsRequest(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	assignedTo: SerializeAsAny[Optional[Identity]] = Field(default=None,alias="assignedTo",)
	closedDateTime: Optional[datetime] = Field(default=None,alias="closedDateTime",)
	contentQuery: Optional[str] = Field(default=None,alias="contentQuery",)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	dataSubject: Optional[DataSubject] = Field(default=None,alias="dataSubject",)
	dataSubjectType: Optional[DataSubjectType] = Field(default=None,alias="dataSubjectType",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	externalId: Optional[str] = Field(default=None,alias="externalId",)
	history: Optional[list[SubjectRightsRequestHistory]] = Field(default=None,alias="history",)
	includeAllVersions: Optional[bool] = Field(default=None,alias="includeAllVersions",)
	includeAuthoredContent: Optional[bool] = Field(default=None,alias="includeAuthoredContent",)
	insight: Optional[SubjectRightsRequestDetail] = Field(default=None,alias="insight",)
	internalDueDateTime: Optional[datetime] = Field(default=None,alias="internalDueDateTime",)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	mailboxLocations: SerializeAsAny[Optional[SubjectRightsRequestMailboxLocation]] = Field(default=None,alias="mailboxLocations",)
	pauseAfterEstimate: Optional[bool] = Field(default=None,alias="pauseAfterEstimate",)
	regulations: Optional[list[str]] = Field(default=None,alias="regulations",)
	siteLocations: SerializeAsAny[Optional[SubjectRightsRequestSiteLocation]] = Field(default=None,alias="siteLocations",)
	stages: Optional[list[SubjectRightsRequestStageDetail]] = Field(default=None,alias="stages",)
	status: Optional[SubjectRightsRequestStatus] = Field(default=None,alias="status",)
	type: Optional[SubjectRightsRequestType] = Field(default=None,alias="type",)
	approvers: Optional[list[User]] = Field(default=None,alias="approvers",)
	collaborators: Optional[list[User]] = Field(default=None,alias="collaborators",)
	notes: Optional[list[AuthoredNote]] = Field(default=None,alias="notes",)
	team: Optional[Team] = Field(default=None,alias="team",)

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

