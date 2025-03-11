from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AndroidManagedStoreApp(BaseModel):
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
	appIdentifier: Optional[str] = Field(alias="appIdentifier",default=None,)
	appStoreUrl: Optional[str] = Field(alias="appStoreUrl",default=None,)
	appTracks: Optional[list[AndroidManagedStoreAppTrack]] = Field(alias="appTracks",default=None,)
	isPrivate: Optional[bool] = Field(alias="isPrivate",default=None,)
	isSystemApp: Optional[bool] = Field(alias="isSystemApp",default=None,)
	packageId: Optional[str] = Field(alias="packageId",default=None,)
	supportsOemConfig: Optional[bool] = Field(alias="supportsOemConfig",default=None,)
	totalLicenseCount: Optional[int] = Field(alias="totalLicenseCount",default=None,)
	usedLicenseCount: Optional[int] = Field(alias="usedLicenseCount",default=None,)

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
			if mapping_key == "#microsoft.graph.androidManagedStoreWebApp":
				from .android_managed_store_web_app import AndroidManagedStoreWebApp
				return AndroidManagedStoreWebApp.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .mime_content import MimeContent
from .mobile_app_publishing_state import MobileAppPublishingState
from .mobile_app_assignment import MobileAppAssignment
from .mobile_app_category import MobileAppCategory
from .mobile_app_relationship import MobileAppRelationship
from .android_managed_store_app_track import AndroidManagedStoreAppTrack

