from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class Training(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.training"] = Field(alias="@odata.type",)
	availabilityStatus: Optional[TrainingAvailabilityStatus | str] = Field(alias="availabilityStatus", default=None,)
	createdBy: Optional[EmailIdentity] = Field(alias="createdBy", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	customUrl: Optional[str] = Field(alias="customUrl", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	durationInMinutes: Optional[int] = Field(alias="durationInMinutes", default=None,)
	hasEvaluation: Optional[bool] = Field(alias="hasEvaluation", default=None,)
	lastModifiedBy: Optional[EmailIdentity] = Field(alias="lastModifiedBy", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	source: Optional[SimulationContentSource | str] = Field(alias="source", default=None,)
	supportedLocales: Optional[list[str]] = Field(alias="supportedLocales", default=None,)
	tags: Optional[list[str]] = Field(alias="tags", default=None,)
	type: Optional[TrainingType | str] = Field(alias="type", default=None,)
	languageDetails: Optional[list[TrainingLanguageDetail]] = Field(alias="languageDetails", default=None,)

from .training_availability_status import TrainingAvailabilityStatus
from .email_identity import EmailIdentity
from .simulation_content_source import SimulationContentSource
from .training_type import TrainingType
from .training_language_detail import TrainingLanguageDetail
