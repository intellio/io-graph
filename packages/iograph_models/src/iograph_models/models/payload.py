from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Payload(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	brand: Optional[PayloadBrand] = Field(default=None,alias="brand",)
	complexity: Optional[PayloadComplexity] = Field(default=None,alias="complexity",)
	createdBy: Optional[EmailIdentity] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	detail: SerializeAsAny[Optional[PayloadDetail]] = Field(default=None,alias="detail",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	industry: Optional[PayloadIndustry] = Field(default=None,alias="industry",)
	isAutomated: Optional[bool] = Field(default=None,alias="isAutomated",)
	isControversial: Optional[bool] = Field(default=None,alias="isControversial",)
	isCurrentEvent: Optional[bool] = Field(default=None,alias="isCurrentEvent",)
	language: Optional[str] = Field(default=None,alias="language",)
	lastModifiedBy: Optional[EmailIdentity] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	payloadTags: Optional[list[str]] = Field(default=None,alias="payloadTags",)
	platform: Optional[PayloadDeliveryPlatform] = Field(default=None,alias="platform",)
	predictedCompromiseRate: float | str | ReferenceNumeric
	simulationAttackType: Optional[SimulationAttackType] = Field(default=None,alias="simulationAttackType",)
	source: Optional[SimulationContentSource] = Field(default=None,alias="source",)
	status: Optional[SimulationContentStatus] = Field(default=None,alias="status",)
	technique: Optional[SimulationAttackTechnique] = Field(default=None,alias="technique",)
	theme: Optional[PayloadTheme] = Field(default=None,alias="theme",)

from .payload_brand import PayloadBrand
from .payload_complexity import PayloadComplexity
from .email_identity import EmailIdentity
from .payload_detail import PayloadDetail
from .payload_industry import PayloadIndustry
from .email_identity import EmailIdentity
from .payload_delivery_platform import PayloadDeliveryPlatform
from .reference_numeric import ReferenceNumeric
from .simulation_attack_type import SimulationAttackType
from .simulation_content_source import SimulationContentSource
from .simulation_content_status import SimulationContentStatus
from .simulation_attack_technique import SimulationAttackTechnique
from .payload_theme import PayloadTheme

