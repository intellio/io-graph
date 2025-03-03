from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from datetime import datetime
from pydantic import BaseModel, Field


class ManagedEBook(BaseModel):
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
			if mapping_key == "#microsoft.graph.iosVppEBook":
				from .ios_vpp_e_book import IosVppEBook
				return IosVppEBook.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .mime_content import MimeContent
from .managed_e_book_assignment import ManagedEBookAssignment
from .device_install_state import DeviceInstallState
from .e_book_install_summary import EBookInstallSummary
from .user_install_state_summary import UserInstallStateSummary

