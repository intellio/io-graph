from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SubjectRightsRequest(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	assignedTo: Optional[Identity] = Field(default=None,alias="assignedTo",)
	closedDateTime: Optional[datetime] = Field(default=None,alias="closedDateTime",)
	contentQuery: Optional[str] = Field(default=None,alias="contentQuery",)
	createdBy: Optional[IdentitySet] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	dataSubject: Optional[DataSubject] = Field(default=None,alias="dataSubject",)
	dataSubjectType: Optional[DataSubjectType] = Field(default=None,alias="dataSubjectType",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	externalId: Optional[str] = Field(default=None,alias="externalId",)
	history: list[SubjectRightsRequestHistory] = Field(alias="history",)
	includeAllVersions: Optional[bool] = Field(default=None,alias="includeAllVersions",)
	includeAuthoredContent: Optional[bool] = Field(default=None,alias="includeAuthoredContent",)
	insight: Optional[SubjectRightsRequestDetail] = Field(default=None,alias="insight",)
	internalDueDateTime: Optional[datetime] = Field(default=None,alias="internalDueDateTime",)
	lastModifiedBy: Optional[IdentitySet] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	mailboxLocations: Optional[SubjectRightsRequestMailboxLocation] = Field(default=None,alias="mailboxLocations",)
	pauseAfterEstimate: Optional[bool] = Field(default=None,alias="pauseAfterEstimate",)
	regulations: list[Optional[str]] = Field(alias="regulations",)
	siteLocations: Optional[SubjectRightsRequestSiteLocation] = Field(default=None,alias="siteLocations",)
	stages: list[SubjectRightsRequestStageDetail] = Field(alias="stages",)
	status: Optional[SubjectRightsRequestStatus] = Field(default=None,alias="status",)
	type: Optional[SubjectRightsRequestType] = Field(default=None,alias="type",)
	approvers: list[User] = Field(alias="approvers",)
	collaborators: list[User] = Field(alias="collaborators",)
	notes: list[AuthoredNote] = Field(alias="notes",)
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

