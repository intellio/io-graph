from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from datetime import datetime
from pydantic import BaseModel, Field


class MobileApp(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	developer: Optional[str] = Field(default=None,alias="developer",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	informationUrl: Optional[str] = Field(default=None,alias="informationUrl",)
	isFeatured: Optional[bool] = Field(default=None,alias="isFeatured",)
	largeIcon: Optional[MimeContent] = Field(default=None,alias="largeIcon",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	notes: Optional[str] = Field(default=None,alias="notes",)
	owner: Optional[str] = Field(default=None,alias="owner",)
	privacyInformationUrl: Optional[str] = Field(default=None,alias="privacyInformationUrl",)
	publisher: Optional[str] = Field(default=None,alias="publisher",)
	publishingState: Optional[MobileAppPublishingState] = Field(default=None,alias="publishingState",)
	assignments: list[MobileAppAssignment] = Field(alias="assignments",)
	categories: list[MobileAppCategory] = Field(alias="categories",)

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
			if mapping_key == "#microsoft.graph.managedApp":
				from .managed_app import ManagedApp
				return ManagedApp.model_validate(data)
			if mapping_key == "#microsoft.graph.managedAndroidStoreApp":
				from .managed_android_store_app import ManagedAndroidStoreApp
				return ManagedAndroidStoreApp.model_validate(data)
			if mapping_key == "#microsoft.graph.managedIOSStoreApp":
				from .managed_i_o_s_store_app import ManagedIOSStoreApp
				return ManagedIOSStoreApp.model_validate(data)
			if mapping_key == "#microsoft.graph.managedMobileLobApp":
				from .managed_mobile_lob_app import ManagedMobileLobApp
				return ManagedMobileLobApp.model_validate(data)
			if mapping_key == "#microsoft.graph.managedAndroidLobApp":
				from .managed_android_lob_app import ManagedAndroidLobApp
				return ManagedAndroidLobApp.model_validate(data)
			if mapping_key == "#microsoft.graph.managedIOSLobApp":
				from .managed_i_o_s_lob_app import ManagedIOSLobApp
				return ManagedIOSLobApp.model_validate(data)
			if mapping_key == "#microsoft.graph.microsoftStoreForBusinessApp":
				from .microsoft_store_for_business_app import MicrosoftStoreForBusinessApp
				return MicrosoftStoreForBusinessApp.model_validate(data)
			if mapping_key == "#microsoft.graph.mobileLobApp":
				from .mobile_lob_app import MobileLobApp
				return MobileLobApp.model_validate(data)
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

