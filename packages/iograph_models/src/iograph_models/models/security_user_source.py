from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityUserSource(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	holdStatus: Optional[SecurityDataSourceHoldStatus | str] = Field(alias="holdStatus",default=None,)
	email: Optional[str] = Field(alias="email",default=None,)
	includedSources: Optional[SecuritySourceType | str] = Field(alias="includedSources",default=None,)
	siteWebUrl: Optional[str] = Field(alias="siteWebUrl",default=None,)

from .identity_set import IdentitySet
from .security_data_source_hold_status import SecurityDataSourceHoldStatus
from .security_source_type import SecuritySourceType

