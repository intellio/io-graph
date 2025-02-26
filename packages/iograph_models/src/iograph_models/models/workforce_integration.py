from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class WorkforceIntegration(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdBy: Optional[IdentitySet] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	lastModifiedBy: Optional[IdentitySet] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	apiVersion: Optional[int] = Field(default=None,alias="apiVersion",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	eligibilityFilteringEnabledEntities: Optional[EligibilityFilteringEnabledEntities] = Field(default=None,alias="eligibilityFilteringEnabledEntities",)
	encryption: Optional[WorkforceIntegrationEncryption] = Field(default=None,alias="encryption",)
	isActive: Optional[bool] = Field(default=None,alias="isActive",)
	supportedEntities: Optional[WorkforceIntegrationSupportedEntities] = Field(default=None,alias="supportedEntities",)
	url: Optional[str] = Field(default=None,alias="url",)

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .eligibility_filtering_enabled_entities import EligibilityFilteringEnabledEntities
from .workforce_integration_encryption import WorkforceIntegrationEncryption
from .workforce_integration_supported_entities import WorkforceIntegrationSupportedEntities

