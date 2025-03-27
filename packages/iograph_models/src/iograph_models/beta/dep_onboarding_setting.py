from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DepOnboardingSetting(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	appleIdentifier: Optional[str] = Field(alias="appleIdentifier", default=None,)
	dataSharingConsentGranted: Optional[bool] = Field(alias="dataSharingConsentGranted", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	lastSuccessfulSyncDateTime: Optional[datetime] = Field(alias="lastSuccessfulSyncDateTime", default=None,)
	lastSyncErrorCode: Optional[int] = Field(alias="lastSyncErrorCode", default=None,)
	lastSyncTriggeredDateTime: Optional[datetime] = Field(alias="lastSyncTriggeredDateTime", default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds", default=None,)
	shareTokenWithSchoolDataSyncService: Optional[bool] = Field(alias="shareTokenWithSchoolDataSyncService", default=None,)
	syncedDeviceCount: Optional[int] = Field(alias="syncedDeviceCount", default=None,)
	tokenExpirationDateTime: Optional[datetime] = Field(alias="tokenExpirationDateTime", default=None,)
	tokenName: Optional[str] = Field(alias="tokenName", default=None,)
	tokenType: Optional[DepTokenType | str] = Field(alias="tokenType", default=None,)
	defaultIosEnrollmentProfile: Optional[DepIOSEnrollmentProfile] = Field(alias="defaultIosEnrollmentProfile", default=None,)
	defaultMacOsEnrollmentProfile: Optional[DepMacOSEnrollmentProfile] = Field(alias="defaultMacOsEnrollmentProfile", default=None,)
	defaultTvOSEnrollmentProfile: Optional[DepTvOSEnrollmentProfile] = Field(alias="defaultTvOSEnrollmentProfile", default=None,)
	defaultVisionOSEnrollmentProfile: Optional[DepVisionOSEnrollmentProfile] = Field(alias="defaultVisionOSEnrollmentProfile", default=None,)
	enrollmentProfiles: Optional[list[Annotated[Union[DepEnrollmentBaseProfile, DepIOSEnrollmentProfile, DepMacOSEnrollmentProfile, DepEnrollmentProfile, DepTvOSEnrollmentProfile, DepVisionOSEnrollmentProfile],Field(discriminator="odata_type")]]] = Field(alias="enrollmentProfiles", default=None,)
	importedAppleDeviceIdentities: Optional[list[Annotated[Union[ImportedAppleDeviceIdentityResult],Field(discriminator="odata_type")]]] = Field(alias="importedAppleDeviceIdentities", default=None,)

from .dep_token_type import DepTokenType
from .dep_i_o_s_enrollment_profile import DepIOSEnrollmentProfile
from .dep_mac_o_s_enrollment_profile import DepMacOSEnrollmentProfile
from .dep_tv_o_s_enrollment_profile import DepTvOSEnrollmentProfile
from .dep_vision_o_s_enrollment_profile import DepVisionOSEnrollmentProfile
from .dep_enrollment_base_profile import DepEnrollmentBaseProfile
from .dep_i_o_s_enrollment_profile import DepIOSEnrollmentProfile
from .dep_mac_o_s_enrollment_profile import DepMacOSEnrollmentProfile
from .dep_enrollment_profile import DepEnrollmentProfile
from .dep_tv_o_s_enrollment_profile import DepTvOSEnrollmentProfile
from .dep_vision_o_s_enrollment_profile import DepVisionOSEnrollmentProfile
from .imported_apple_device_identity_result import ImportedAppleDeviceIdentityResult

