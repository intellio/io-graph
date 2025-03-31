from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field


class MacOsVppApp(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.macOsVppApp"] = Field(alias="@odata.type", default="#microsoft.graph.macOsVppApp")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	dependentAppCount: Optional[int] = Field(alias="dependentAppCount", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	developer: Optional[str] = Field(alias="developer", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	informationUrl: Optional[str] = Field(alias="informationUrl", default=None,)
	isAssigned: Optional[bool] = Field(alias="isAssigned", default=None,)
	isFeatured: Optional[bool] = Field(alias="isFeatured", default=None,)
	largeIcon: Optional[MimeContent] = Field(alias="largeIcon", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	notes: Optional[str] = Field(alias="notes", default=None,)
	owner: Optional[str] = Field(alias="owner", default=None,)
	privacyInformationUrl: Optional[str] = Field(alias="privacyInformationUrl", default=None,)
	publisher: Optional[str] = Field(alias="publisher", default=None,)
	publishingState: Optional[MobileAppPublishingState | str] = Field(alias="publishingState", default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds", default=None,)
	supersededAppCount: Optional[int] = Field(alias="supersededAppCount", default=None,)
	supersedingAppCount: Optional[int] = Field(alias="supersedingAppCount", default=None,)
	uploadState: Optional[int] = Field(alias="uploadState", default=None,)
	assignments: Optional[list[MobileAppAssignment]] = Field(alias="assignments", default=None,)
	categories: Optional[list[MobileAppCategory]] = Field(alias="categories", default=None,)
	relationships: Optional[list[Annotated[Union[MobileAppDependency, MobileAppSupersedence],Field(discriminator="odata_type")]]] = Field(alias="relationships", default=None,)
	appStoreUrl: Optional[str] = Field(alias="appStoreUrl", default=None,)
	bundleId: Optional[str] = Field(alias="bundleId", default=None,)
	licensingType: Optional[VppLicensingType] = Field(alias="licensingType", default=None,)
	releaseDateTime: Optional[datetime] = Field(alias="releaseDateTime", default=None,)
	revokeLicenseActionResults: Optional[list[MacOsVppAppRevokeLicensesActionResult]] = Field(alias="revokeLicenseActionResults", default=None,)
	totalLicenseCount: Optional[int] = Field(alias="totalLicenseCount", default=None,)
	usedLicenseCount: Optional[int] = Field(alias="usedLicenseCount", default=None,)
	vppTokenAccountType: Optional[VppTokenAccountType | str] = Field(alias="vppTokenAccountType", default=None,)
	vppTokenAppleId: Optional[str] = Field(alias="vppTokenAppleId", default=None,)
	vppTokenDisplayName: Optional[str] = Field(alias="vppTokenDisplayName", default=None,)
	vppTokenId: Optional[str] = Field(alias="vppTokenId", default=None,)
	vppTokenOrganizationName: Optional[str] = Field(alias="vppTokenOrganizationName", default=None,)
	assignedLicenses: Optional[list[MacOsVppAppAssignedLicense]] = Field(alias="assignedLicenses", default=None,)

from .mime_content import MimeContent
from .mobile_app_publishing_state import MobileAppPublishingState
from .mobile_app_assignment import MobileAppAssignment
from .mobile_app_category import MobileAppCategory
from .mobile_app_dependency import MobileAppDependency
from .mobile_app_supersedence import MobileAppSupersedence
from .vpp_licensing_type import VppLicensingType
from .mac_os_vpp_app_revoke_licenses_action_result import MacOsVppAppRevokeLicensesActionResult
from .vpp_token_account_type import VppTokenAccountType
from .mac_os_vpp_app_assigned_license import MacOsVppAppAssignedLicense
