from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class Recommendation(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.recommendation"] = Field(alias="@odata.type", default="#microsoft.graph.recommendation")
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

from .action_step import ActionStep
from .recommendation_category import RecommendationCategory
from .reference_numeric import ReferenceNumeric
from .recommendation_feature_areas import RecommendationFeatureAreas
from .recommendation_priority import RecommendationPriority
from .recommendation_type import RecommendationType
from .required_licenses import RequiredLicenses
from .recommendation_status import RecommendationStatus
from .impacted_resource import ImpactedResource
