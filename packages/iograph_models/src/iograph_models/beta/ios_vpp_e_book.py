from __future__ import annotations
from uuid import UUID
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class IosVppEBook(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.iosVppEBook"] = Field(alias="@odata.type", default="#microsoft.graph.iosVppEBook")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	informationUrl: Optional[str] = Field(alias="informationUrl", default=None,)
	largeCover: Optional[MimeContent] = Field(alias="largeCover", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	privacyInformationUrl: Optional[str] = Field(alias="privacyInformationUrl", default=None,)
	publishedDateTime: Optional[datetime] = Field(alias="publishedDateTime", default=None,)
	publisher: Optional[str] = Field(alias="publisher", default=None,)
	assignments: Optional[list[Annotated[Union[IosVppEBookAssignment]],Field(discriminator="odata_type")]]] = Field(alias="assignments", default=None,)
	categories: Optional[list[ManagedEBookCategory]] = Field(alias="categories", default=None,)
	deviceStates: Optional[list[DeviceInstallState]] = Field(alias="deviceStates", default=None,)
	installSummary: Optional[EBookInstallSummary] = Field(alias="installSummary", default=None,)
	userStateSummary: Optional[list[UserInstallStateSummary]] = Field(alias="userStateSummary", default=None,)
	appleId: Optional[str] = Field(alias="appleId", default=None,)
	genres: Optional[list[str]] = Field(alias="genres", default=None,)
	language: Optional[str] = Field(alias="language", default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds", default=None,)
	seller: Optional[str] = Field(alias="seller", default=None,)
	totalLicenseCount: Optional[int] = Field(alias="totalLicenseCount", default=None,)
	usedLicenseCount: Optional[int] = Field(alias="usedLicenseCount", default=None,)
	vppOrganizationName: Optional[str] = Field(alias="vppOrganizationName", default=None,)
	vppTokenId: Optional[UUID] = Field(alias="vppTokenId", default=None,)

from .mime_content import MimeContent
from .ios_vpp_e_book_assignment import IosVppEBookAssignment
from .managed_e_book_category import ManagedEBookCategory
from .device_install_state import DeviceInstallState
from .e_book_install_summary import EBookInstallSummary
from .user_install_state_summary import UserInstallStateSummary

