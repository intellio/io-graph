from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MacOSPrivacyAccessControlItem(BaseModel):
	accessibility: Optional[Enablement | str] = Field(alias="accessibility", default=None,)
	addressBook: Optional[Enablement | str] = Field(alias="addressBook", default=None,)
	appleEventsAllowedReceivers: Optional[list[MacOSAppleEventReceiver]] = Field(alias="appleEventsAllowedReceivers", default=None,)
	blockCamera: Optional[bool] = Field(alias="blockCamera", default=None,)
	blockListenEvent: Optional[bool] = Field(alias="blockListenEvent", default=None,)
	blockMicrophone: Optional[bool] = Field(alias="blockMicrophone", default=None,)
	blockScreenCapture: Optional[bool] = Field(alias="blockScreenCapture", default=None,)
	calendar: Optional[Enablement | str] = Field(alias="calendar", default=None,)
	codeRequirement: Optional[str] = Field(alias="codeRequirement", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	fileProviderPresence: Optional[Enablement | str] = Field(alias="fileProviderPresence", default=None,)
	identifier: Optional[str] = Field(alias="identifier", default=None,)
	identifierType: Optional[MacOSProcessIdentifierType | str] = Field(alias="identifierType", default=None,)
	mediaLibrary: Optional[Enablement | str] = Field(alias="mediaLibrary", default=None,)
	photos: Optional[Enablement | str] = Field(alias="photos", default=None,)
	postEvent: Optional[Enablement | str] = Field(alias="postEvent", default=None,)
	reminders: Optional[Enablement | str] = Field(alias="reminders", default=None,)
	speechRecognition: Optional[Enablement | str] = Field(alias="speechRecognition", default=None,)
	staticCodeValidation: Optional[bool] = Field(alias="staticCodeValidation", default=None,)
	systemPolicyAllFiles: Optional[Enablement | str] = Field(alias="systemPolicyAllFiles", default=None,)
	systemPolicyDesktopFolder: Optional[Enablement | str] = Field(alias="systemPolicyDesktopFolder", default=None,)
	systemPolicyDocumentsFolder: Optional[Enablement | str] = Field(alias="systemPolicyDocumentsFolder", default=None,)
	systemPolicyDownloadsFolder: Optional[Enablement | str] = Field(alias="systemPolicyDownloadsFolder", default=None,)
	systemPolicyNetworkVolumes: Optional[Enablement | str] = Field(alias="systemPolicyNetworkVolumes", default=None,)
	systemPolicyRemovableVolumes: Optional[Enablement | str] = Field(alias="systemPolicyRemovableVolumes", default=None,)
	systemPolicySystemAdminFiles: Optional[Enablement | str] = Field(alias="systemPolicySystemAdminFiles", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .enablement import Enablement
from .mac_o_s_apple_event_receiver import MacOSAppleEventReceiver
from .mac_o_s_process_identifier_type import MacOSProcessIdentifierType
