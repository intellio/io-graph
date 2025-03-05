from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class VppToken(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	appleId: Optional[str] = Field(default=None,alias="appleId",)
	automaticallyUpdateApps: Optional[bool] = Field(default=None,alias="automaticallyUpdateApps",)
	countryOrRegion: Optional[str] = Field(default=None,alias="countryOrRegion",)
	expirationDateTime: Optional[datetime] = Field(default=None,alias="expirationDateTime",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	lastSyncDateTime: Optional[datetime] = Field(default=None,alias="lastSyncDateTime",)
	lastSyncStatus: Optional[VppTokenSyncStatus] = Field(default=None,alias="lastSyncStatus",)
	organizationName: Optional[str] = Field(default=None,alias="organizationName",)
	state: Optional[VppTokenState] = Field(default=None,alias="state",)
	token: Optional[str] = Field(default=None,alias="token",)
	vppTokenAccountType: Optional[VppTokenAccountType] = Field(default=None,alias="vppTokenAccountType",)

from .vpp_token_sync_status import VppTokenSyncStatus
from .vpp_token_state import VppTokenState
from .vpp_token_account_type import VppTokenAccountType

