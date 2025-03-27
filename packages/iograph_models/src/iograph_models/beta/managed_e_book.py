from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedEBook(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	informationUrl: Optional[str] = Field(alias="informationUrl", default=None,)
	largeCover: Optional[MimeContent] = Field(alias="largeCover", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	privacyInformationUrl: Optional[str] = Field(alias="privacyInformationUrl", default=None,)
	publishedDateTime: Optional[datetime] = Field(alias="publishedDateTime", default=None,)
	publisher: Optional[str] = Field(alias="publisher", default=None,)
	assignments: Optional[list[Annotated[Union[IosVppEBookAssignment],Field(discriminator="odata_type")]]] = Field(alias="assignments", default=None,)
	categories: Optional[list[ManagedEBookCategory]] = Field(alias="categories", default=None,)
	deviceStates: Optional[list[DeviceInstallState]] = Field(alias="deviceStates", default=None,)
	installSummary: Optional[EBookInstallSummary] = Field(alias="installSummary", default=None,)
	userStateSummary: Optional[list[UserInstallStateSummary]] = Field(alias="userStateSummary", default=None,)

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
from .ios_vpp_e_book_assignment import IosVppEBookAssignment
from .managed_e_book_category import ManagedEBookCategory
from .device_install_state import DeviceInstallState
from .e_book_install_summary import EBookInstallSummary
from .user_install_state_summary import UserInstallStateSummary

