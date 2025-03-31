from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ImpactedResource(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.impactedResource"] = Field(alias="@odata.type",)
	addedDateTime: Optional[datetime] = Field(alias="addedDateTime", default=None,)
	additionalDetails: Optional[list[KeyValue]] = Field(alias="additionalDetails", default=None,)
	apiUrl: Optional[str] = Field(alias="apiUrl", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastModifiedBy: Optional[str] = Field(alias="lastModifiedBy", default=None,)
	lastModifiedDateTime: Optional[str] = Field(alias="lastModifiedDateTime", default=None,)
	owner: Optional[str] = Field(alias="owner", default=None,)
	portalUrl: Optional[str] = Field(alias="portalUrl", default=None,)
	postponeUntilDateTime: Optional[datetime] = Field(alias="postponeUntilDateTime", default=None,)
	rank: Optional[int] = Field(alias="rank", default=None,)
	recommendationId: Optional[str] = Field(alias="recommendationId", default=None,)
	resourceType: Optional[str] = Field(alias="resourceType", default=None,)
	status: Optional[RecommendationStatus | str] = Field(alias="status", default=None,)
	subjectId: Optional[str] = Field(alias="subjectId", default=None,)

from .key_value import KeyValue
from .recommendation_status import RecommendationStatus
