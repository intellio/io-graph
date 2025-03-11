from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class MobileLobApp(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	dependentAppCount: Optional[int] = Field(alias="dependentAppCount",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	developer: Optional[str] = Field(alias="developer",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	informationUrl: Optional[str] = Field(alias="informationUrl",default=None,)
	isAssigned: Optional[bool] = Field(alias="isAssigned",default=None,)
	isFeatured: Optional[bool] = Field(alias="isFeatured",default=None,)
	largeIcon: Optional[MimeContent] = Field(alias="largeIcon",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	notes: Optional[str] = Field(alias="notes",default=None,)
	owner: Optional[str] = Field(alias="owner",default=None,)
	privacyInformationUrl: Optional[str] = Field(alias="privacyInformationUrl",default=None,)
	publisher: Optional[str] = Field(alias="publisher",default=None,)
	publishingState: Optional[MobileAppPublishingState | str] = Field(alias="publishingState",default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds",default=None,)
	supersededAppCount: Optional[int] = Field(alias="supersededAppCount",default=None,)
	supersedingAppCount: Optional[int] = Field(alias="supersedingAppCount",default=None,)
	uploadState: Optional[int] = Field(alias="uploadState",default=None,)
	assignments: Optional[list[MobileAppAssignment]] = Field(alias="assignments",default=None,)
	categories: Optional[list[MobileAppCategory]] = Field(alias="categories",default=None,)
	relationships: SerializeAsAny[Optional[list[MobileAppRelationship]]] = Field(alias="relationships",default=None,)
	committedContentVersion: Optional[str] = Field(alias="committedContentVersion",default=None,)
	fileName: Optional[str] = Field(alias="fileName",default=None,)
	size: Optional[int] = Field(alias="size",default=None,)
	contentVersions: Optional[list[MobileAppContent]] = Field(alias="contentVersions",default=None,)

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
			if mapping_key == "#microsoft.graph.macOSPkgApp":
				from .mac_o_s_pkg_app import MacOSPkgApp
				return MacOSPkgApp.model_validate(data)
			if mapping_key == "#microsoft.graph.win32LobApp":
				from .win32_lob_app import Win32LobApp
				return Win32LobApp.model_validate(data)
			if mapping_key == "#microsoft.graph.win32CatalogApp":
				from .win32_catalog_app import Win32CatalogApp
				return Win32CatalogApp.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsAppX":
				from .windows_app_x import WindowsAppX
				return WindowsAppX.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsMobileMSI":
				from .windows_mobile_m_s_i import WindowsMobileMSI
				return WindowsMobileMSI.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsPhone81AppX":
				from .windows_phone81_app_x import WindowsPhone81AppX
				return WindowsPhone81AppX.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsPhone81AppXBundle":
				from .windows_phone81_app_x_bundle import WindowsPhone81AppXBundle
				return WindowsPhone81AppXBundle.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsPhoneXAP":
				from .windows_phone_x_a_p import WindowsPhoneXAP
				return WindowsPhoneXAP.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsUniversalAppX":
				from .windows_universal_app_x import WindowsUniversalAppX
				return WindowsUniversalAppX.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .mime_content import MimeContent
from .mobile_app_publishing_state import MobileAppPublishingState
from .mobile_app_assignment import MobileAppAssignment
from .mobile_app_category import MobileAppCategory
from .mobile_app_relationship import MobileAppRelationship
from .mobile_app_content import MobileAppContent

