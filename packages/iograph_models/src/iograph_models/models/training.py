from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class Training(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	availabilityStatus: Optional[TrainingAvailabilityStatus] = Field(default=None,alias="availabilityStatus",)
	createdBy: Optional[EmailIdentity] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	durationInMinutes: Optional[int] = Field(default=None,alias="durationInMinutes",)
	hasEvaluation: Optional[bool] = Field(default=None,alias="hasEvaluation",)
	lastModifiedBy: Optional[EmailIdentity] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	source: Optional[SimulationContentSource] = Field(default=None,alias="source",)
	supportedLocales: Optional[list[str]] = Field(default=None,alias="supportedLocales",)
	tags: Optional[list[str]] = Field(default=None,alias="tags",)
	type: Optional[TrainingType] = Field(default=None,alias="type",)
	languageDetails: Optional[list[TrainingLanguageDetail]] = Field(default=None,alias="languageDetails",)

from .training_availability_status import TrainingAvailabilityStatus
from .email_identity import EmailIdentity
from .email_identity import EmailIdentity
from .simulation_content_source import SimulationContentSource
from .training_type import TrainingType
from .training_language_detail import TrainingLanguageDetail

