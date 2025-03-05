from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityUnifiedGroupSource(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	holdStatus: Optional[str | SecurityDataSourceHoldStatus] = Field(alias="holdStatus",default=None,)
	includedSources: Optional[str | SecuritySourceType] = Field(alias="includedSources",default=None,)
	group: Optional[Group] = Field(alias="group",default=None,)

from .identity_set import IdentitySet
from .security_data_source_hold_status import SecurityDataSourceHoldStatus
from .security_source_type import SecuritySourceType
from .group import Group

