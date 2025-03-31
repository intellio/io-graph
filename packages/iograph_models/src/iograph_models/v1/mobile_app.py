from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class MobileApp(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	developer: Optional[str] = Field(alias="developer", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	informationUrl: Optional[str] = Field(alias="informationUrl", default=None,)
	isFeatured: Optional[bool] = Field(alias="isFeatured", default=None,)
	largeIcon: Optional[MimeContent] = Field(alias="largeIcon", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	notes: Optional[str] = Field(alias="notes", default=None,)
	owner: Optional[str] = Field(alias="owner", default=None,)
	privacyInformationUrl: Optional[str] = Field(alias="privacyInformationUrl", default=None,)
	publisher: Optional[str] = Field(alias="publisher", default=None,)
	publishingState: Optional[MobileAppPublishingState | str] = Field(alias="publishingState", default=None,)
	assignments: Optional[list[MobileAppAssignment]] = Field(alias="assignments", default=None,)
	categories: Optional[list[MobileAppCategory]] = Field(alias="categories", default=None,)

	@model_validator(mode="wrap")
	def convert_discriminator_class(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
		try:
			# check with parent model to catch any errors
			parent_validated_model = handler(data)
			# check if the discriminator field is present
			if "@odata.type" not in data:
				return parent_validated_model
			# get the discriminator value
			mapping_key = data["@odata.type"]
			if mapping_key == "#microsoft.graph.androidStoreApp":
				from .android_store_app import AndroidStoreApp
				return AndroidStoreApp.model_validate(data)
			if mapping_key == "#microsoft.graph.iosiPadOSWebClip":
				from .iosi_pad_o_s_web_clip import IosiPadOSWebClip
				return IosiPadOSWebClip.model_validate(data)
			if mapping_key == "#microsoft.graph.iosStoreApp":
				from .ios_store_app import IosStoreApp
				return IosStoreApp.model_validate(data)
			if mapping_key == "#microsoft.graph.iosVppApp":
				from .ios_vpp_app import IosVppApp
				return IosVppApp.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSMicrosoftDefenderApp":
				from .mac_o_s_microsoft_defender_app import MacOSMicrosoftDefenderApp
				return MacOSMicrosoftDefenderApp.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSMicrosoftEdgeApp":
				from .mac_o_s_microsoft_edge_app import MacOSMicrosoftEdgeApp
				return MacOSMicrosoftEdgeApp.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSOfficeSuiteApp":
				from .mac_o_s_office_suite_app import MacOSOfficeSuiteApp
				return MacOSOfficeSuiteApp.model_validate(data)
			if mapping_key == "#microsoft.graph.managedAndroidStoreApp":
				from .managed_android_store_app import ManagedAndroidStoreApp
				return ManagedAndroidStoreApp.model_validate(data)
			if mapping_key == "#microsoft.graph.managedIOSStoreApp":
				from .managed_i_o_s_store_app import ManagedIOSStoreApp
				return ManagedIOSStoreApp.model_validate(data)
			if mapping_key == "#microsoft.graph.managedAndroidLobApp":
				from .managed_android_lob_app import ManagedAndroidLobApp
				return ManagedAndroidLobApp.model_validate(data)
			if mapping_key == "#microsoft.graph.managedIOSLobApp":
				from .managed_i_o_s_lob_app import ManagedIOSLobApp
				return ManagedIOSLobApp.model_validate(data)
			if mapping_key == "#microsoft.graph.microsoftStoreForBusinessApp":
				from .microsoft_store_for_business_app import MicrosoftStoreForBusinessApp
				return MicrosoftStoreForBusinessApp.model_validate(data)
			if mapping_key == "#microsoft.graph.androidLobApp":
				from .android_lob_app import AndroidLobApp
				return AndroidLobApp.model_validate(data)
			if mapping_key == "#microsoft.graph.iosLobApp":
				from .ios_lob_app import IosLobApp
				return IosLobApp.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSDmgApp":
				from .mac_o_s_dmg_app import MacOSDmgApp
				return MacOSDmgApp.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSLobApp":
				from .mac_o_s_lob_app import MacOSLobApp
				return MacOSLobApp.model_validate(data)
			if mapping_key == "#microsoft.graph.win32LobApp":
				from .win32_lob_app import Win32LobApp
				return Win32LobApp.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsAppX":
				from .windows_app_x import WindowsAppX
				return WindowsAppX.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsMobileMSI":
				from .windows_mobile_m_s_i import WindowsMobileMSI
				return WindowsMobileMSI.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsUniversalAppX":
				from .windows_universal_app_x import WindowsUniversalAppX
				return WindowsUniversalAppX.model_validate(data)
			if mapping_key == "#microsoft.graph.webApp":
				from .web_app import WebApp
				return WebApp.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsMicrosoftEdgeApp":
				from .windows_microsoft_edge_app import WindowsMicrosoftEdgeApp
				return WindowsMicrosoftEdgeApp.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsWebApp":
				from .windows_web_app import WindowsWebApp
				return WindowsWebApp.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .mime_content import MimeContent
from .mobile_app_publishing_state import MobileAppPublishingState
from .mobile_app_assignment import MobileAppAssignment
from .mobile_app_category import MobileAppCategory
