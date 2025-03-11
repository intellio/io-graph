from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class VppToken(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	appleId: Optional[str] = Field(alias="appleId",default=None,)
	automaticallyUpdateApps: Optional[bool] = Field(alias="automaticallyUpdateApps",default=None,)
	claimTokenManagementFromExternalMdm: Optional[bool] = Field(alias="claimTokenManagementFromExternalMdm",default=None,)
	countryOrRegion: Optional[str] = Field(alias="countryOrRegion",default=None,)
	dataSharingConsentGranted: Optional[bool] = Field(alias="dataSharingConsentGranted",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	lastSyncDateTime: Optional[datetime] = Field(alias="lastSyncDateTime",default=None,)
	lastSyncStatus: Optional[VppTokenSyncStatus | str] = Field(alias="lastSyncStatus",default=None,)
	locationName: Optional[str] = Field(alias="locationName",default=None,)
	organizationName: Optional[str] = Field(alias="organizationName",default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds",default=None,)
	state: Optional[VppTokenState | str] = Field(alias="state",default=None,)
	token: Optional[str] = Field(alias="token",default=None,)
	tokenActionResults: SerializeAsAny[Optional[list[VppTokenActionResult]]] = Field(alias="tokenActionResults",default=None,)
	vppTokenAccountType: Optional[VppTokenAccountType | str] = Field(alias="vppTokenAccountType",default=None,)

from .vpp_token_sync_status import VppTokenSyncStatus
from .vpp_token_state import VppTokenState
from .vpp_token_action_result import VppTokenActionResult
from .vpp_token_account_type import VppTokenAccountType

