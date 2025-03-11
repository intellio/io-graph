from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AwsExternalSystemAccessFinding(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	accessMethods: Optional[ExternalSystemAccessMethods | str] = Field(alias="accessMethods",default=None,)
	systemWithAccess: Optional[AuthorizationSystemInfo] = Field(alias="systemWithAccess",default=None,)
	trustedIdentityCount: Optional[int] = Field(alias="trustedIdentityCount",default=None,)
	trustsAllIdentities: Optional[bool] = Field(alias="trustsAllIdentities",default=None,)
	affectedSystem: SerializeAsAny[Optional[AuthorizationSystem]] = Field(alias="affectedSystem",default=None,)

from .external_system_access_methods import ExternalSystemAccessMethods
from .authorization_system_info import AuthorizationSystemInfo
from .authorization_system import AuthorizationSystem

