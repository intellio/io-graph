from __future__ import annotations
from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class IosVppEBook(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	informationUrl: Optional[str] = Field(default=None,alias="informationUrl",)
	largeCover: Optional[MimeContent] = Field(default=None,alias="largeCover",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	privacyInformationUrl: Optional[str] = Field(default=None,alias="privacyInformationUrl",)
	publishedDateTime: Optional[datetime] = Field(default=None,alias="publishedDateTime",)
	publisher: Optional[str] = Field(default=None,alias="publisher",)
	assignments: Optional[list[ManagedEBookAssignment]] = Field(default=None,alias="assignments",)
	deviceStates: Optional[list[DeviceInstallState]] = Field(default=None,alias="deviceStates",)
	installSummary: Optional[EBookInstallSummary] = Field(default=None,alias="installSummary",)
	userStateSummary: Optional[list[UserInstallStateSummary]] = Field(default=None,alias="userStateSummary",)
	appleId: Optional[str] = Field(default=None,alias="appleId",)
	genres: Optional[list[str]] = Field(default=None,alias="genres",)
	language: Optional[str] = Field(default=None,alias="language",)
	seller: Optional[str] = Field(default=None,alias="seller",)
	totalLicenseCount: Optional[int] = Field(default=None,alias="totalLicenseCount",)
	usedLicenseCount: Optional[int] = Field(default=None,alias="usedLicenseCount",)
	vppOrganizationName: Optional[str] = Field(default=None,alias="vppOrganizationName",)
	vppTokenId: Optional[UUID] = Field(default=None,alias="vppTokenId",)

from .mime_content import MimeContent
from .managed_e_book_assignment import ManagedEBookAssignment
from .device_install_state import DeviceInstallState
from .e_book_install_summary import EBookInstallSummary
from .user_install_state_summary import UserInstallStateSummary

