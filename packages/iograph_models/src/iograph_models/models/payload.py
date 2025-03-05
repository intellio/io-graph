from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Payload(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	brand: Optional[str | PayloadBrand] = Field(alias="brand",default=None,)
	complexity: Optional[str | PayloadComplexity] = Field(alias="complexity",default=None,)
	createdBy: Optional[EmailIdentity] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	detail: SerializeAsAny[Optional[PayloadDetail]] = Field(alias="detail",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	industry: Optional[str | PayloadIndustry] = Field(alias="industry",default=None,)
	isAutomated: Optional[bool] = Field(alias="isAutomated",default=None,)
	isControversial: Optional[bool] = Field(alias="isControversial",default=None,)
	isCurrentEvent: Optional[bool] = Field(alias="isCurrentEvent",default=None,)
	language: Optional[str] = Field(alias="language",default=None,)
	lastModifiedBy: Optional[EmailIdentity] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	payloadTags: Optional[list[str]] = Field(alias="payloadTags",default=None,)
	platform: Optional[str | PayloadDeliveryPlatform] = Field(alias="platform",default=None,)
	predictedCompromiseRate: float | str | ReferenceNumeric
	simulationAttackType: Optional[str | SimulationAttackType] = Field(alias="simulationAttackType",default=None,)
	source: Optional[str | SimulationContentSource] = Field(alias="source",default=None,)
	status: Optional[str | SimulationContentStatus] = Field(alias="status",default=None,)
	technique: Optional[str | SimulationAttackTechnique] = Field(alias="technique",default=None,)
	theme: Optional[str | PayloadTheme] = Field(alias="theme",default=None,)

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

