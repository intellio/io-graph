from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class WorkforceIntegration(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	apiVersion: Optional[int] = Field(alias="apiVersion",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	eligibilityFilteringEnabledEntities: Optional[str | EligibilityFilteringEnabledEntities] = Field(alias="eligibilityFilteringEnabledEntities",default=None,)
	encryption: Optional[WorkforceIntegrationEncryption] = Field(alias="encryption",default=None,)
	isActive: Optional[bool] = Field(alias="isActive",default=None,)
	supportedEntities: Optional[str | WorkforceIntegrationSupportedEntities] = Field(alias="supportedEntities",default=None,)
	url: Optional[str] = Field(alias="url",default=None,)

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .eligibility_filtering_enabled_entities import EligibilityFilteringEnabledEntities
from .workforce_integration_encryption import WorkforceIntegrationEncryption
from .workforce_integration_supported_entities import WorkforceIntegrationSupportedEntities

