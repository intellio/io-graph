from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class RecommendationBase(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	actionSteps: Optional[list[ActionStep]] = Field(alias="actionSteps", default=None,)
	benefits: Optional[str] = Field(alias="benefits", default=None,)
	category: Optional[RecommendationCategory | str] = Field(alias="category", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	currentScore: float | str | ReferenceNumeric
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	featureAreas: Optional[list[RecommendationFeatureAreas | str]] = Field(alias="featureAreas", default=None,)
	impactStartDateTime: Optional[datetime] = Field(alias="impactStartDateTime", default=None,)
	impactType: Optional[str] = Field(alias="impactType", default=None,)
	insights: Optional[str] = Field(alias="insights", default=None,)
	lastCheckedDateTime: Optional[datetime] = Field(alias="lastCheckedDateTime", default=None,)
	lastModifiedBy: Optional[str] = Field(alias="lastModifiedBy", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	maxScore: float | str | ReferenceNumeric
	postponeUntilDateTime: Optional[datetime] = Field(alias="postponeUntilDateTime", default=None,)
	priority: Optional[RecommendationPriority | str] = Field(alias="priority", default=None,)
	recommendationType: Optional[RecommendationType | str] = Field(alias="recommendationType", default=None,)
	releaseType: Optional[str] = Field(alias="releaseType", default=None,)
	remediationImpact: Optional[str] = Field(alias="remediationImpact", default=None,)
	requiredLicenses: Optional[RequiredLicenses | str] = Field(alias="requiredLicenses", default=None,)
	status: Optional[RecommendationStatus | str] = Field(alias="status", default=None,)
	impactedResources: Optional[list[ImpactedResource]] = Field(alias="impactedResources", default=None,)

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
			if mapping_key == "#microsoft.graph.recommendation":
				from .recommendation import Recommendation
				return Recommendation.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .action_step import ActionStep
from .recommendation_category import RecommendationCategory
from .reference_numeric import ReferenceNumeric
from .recommendation_feature_areas import RecommendationFeatureAreas
from .recommendation_priority import RecommendationPriority
from .recommendation_type import RecommendationType
from .required_licenses import RequiredLicenses
from .recommendation_status import RecommendationStatus
from .impacted_resource import ImpactedResource
