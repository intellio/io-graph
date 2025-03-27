from __future__ import annotations
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ApiApplication(BaseModel):
	acceptMappedClaims: Optional[bool] = Field(alias="acceptMappedClaims", default=None,)
	knownClientApplications: Optional[list[UUID]] = Field(alias="knownClientApplications", default=None,)
	oauth2PermissionScopes: Optional[list[PermissionScope]] = Field(alias="oauth2PermissionScopes", default=None,)
	preAuthorizedApplications: Optional[list[PreAuthorizedApplication]] = Field(alias="preAuthorizedApplications", default=None,)
	requestedAccessTokenVersion: Optional[int] = Field(alias="requestedAccessTokenVersion", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .permission_scope import PermissionScope
from .pre_authorized_application import PreAuthorizedApplication

