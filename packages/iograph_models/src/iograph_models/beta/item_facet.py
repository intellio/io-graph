from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ItemFacet(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	allowedAudiences: Optional[AllowedAudiences | str] = Field(alias="allowedAudiences",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	inference: Optional[InferenceData] = Field(alias="inference",default=None,)
	isSearchable: Optional[bool] = Field(alias="isSearchable",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	source: Optional[PersonDataSources] = Field(alias="source",default=None,)
	sources: Optional[list[ProfileSourceAnnotation]] = Field(alias="sources",default=None,)

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
			if mapping_key == "#microsoft.graph.educationalActivity":
				from .educational_activity import EducationalActivity
				return EducationalActivity.model_validate(data)
			if mapping_key == "#microsoft.graph.itemAddress":
				from .item_address import ItemAddress
				return ItemAddress.model_validate(data)
			if mapping_key == "#microsoft.graph.itemEmail":
				from .item_email import ItemEmail
				return ItemEmail.model_validate(data)
			if mapping_key == "#microsoft.graph.itemPatent":
				from .item_patent import ItemPatent
				return ItemPatent.model_validate(data)
			if mapping_key == "#microsoft.graph.itemPhone":
				from .item_phone import ItemPhone
				return ItemPhone.model_validate(data)
			if mapping_key == "#microsoft.graph.itemPublication":
				from .item_publication import ItemPublication
				return ItemPublication.model_validate(data)
			if mapping_key == "#microsoft.graph.languageProficiency":
				from .language_proficiency import LanguageProficiency
				return LanguageProficiency.model_validate(data)
			if mapping_key == "#microsoft.graph.personAnnotation":
				from .person_annotation import PersonAnnotation
				return PersonAnnotation.model_validate(data)
			if mapping_key == "#microsoft.graph.personAnnualEvent":
				from .person_annual_event import PersonAnnualEvent
				return PersonAnnualEvent.model_validate(data)
			if mapping_key == "#microsoft.graph.personAward":
				from .person_award import PersonAward
				return PersonAward.model_validate(data)
			if mapping_key == "#microsoft.graph.personCertification":
				from .person_certification import PersonCertification
				return PersonCertification.model_validate(data)
			if mapping_key == "#microsoft.graph.personInterest":
				from .person_interest import PersonInterest
				return PersonInterest.model_validate(data)
			if mapping_key == "#microsoft.graph.personName":
				from .person_name import PersonName
				return PersonName.model_validate(data)
			if mapping_key == "#microsoft.graph.personResponsibility":
				from .person_responsibility import PersonResponsibility
				return PersonResponsibility.model_validate(data)
			if mapping_key == "#microsoft.graph.personWebsite":
				from .person_website import PersonWebsite
				return PersonWebsite.model_validate(data)
			if mapping_key == "#microsoft.graph.projectParticipation":
				from .project_participation import ProjectParticipation
				return ProjectParticipation.model_validate(data)
			if mapping_key == "#microsoft.graph.skillProficiency":
				from .skill_proficiency import SkillProficiency
				return SkillProficiency.model_validate(data)
			if mapping_key == "#microsoft.graph.userAccountInformation":
				from .user_account_information import UserAccountInformation
				return UserAccountInformation.model_validate(data)
			if mapping_key == "#microsoft.graph.webAccount":
				from .web_account import WebAccount
				return WebAccount.model_validate(data)
			if mapping_key == "#microsoft.graph.workPosition":
				from .work_position import WorkPosition
				return WorkPosition.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .allowed_audiences import AllowedAudiences
from .identity_set import IdentitySet
from .inference_data import InferenceData
from .identity_set import IdentitySet
from .person_data_sources import PersonDataSources
from .profile_source_annotation import ProfileSourceAnnotation

