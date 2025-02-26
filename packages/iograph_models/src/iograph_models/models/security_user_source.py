from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityUserSource(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdBy: Optional[IdentitySet] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	holdStatus: Optional[SecurityDataSourceHoldStatus] = Field(default=None,alias="holdStatus",)
	email: Optional[str] = Field(default=None,alias="email",)
	includedSources: Optional[SecuritySourceType] = Field(default=None,alias="includedSources",)
	siteWebUrl: Optional[str] = Field(default=None,alias="siteWebUrl",)

from .identity_set import IdentitySet
from .security_data_source_hold_status import SecurityDataSourceHoldStatus
from .security_source_type import SecuritySourceType

