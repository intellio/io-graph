from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class CallRecordsPstnBlockedUsersLogRow(BaseModel):
	blockDateTime: Optional[datetime] = Field(alias="blockDateTime",default=None,)
	blockReason: Optional[str] = Field(alias="blockReason",default=None,)
	remediationId: Optional[str] = Field(alias="remediationId",default=None,)
	userBlockMode: Optional[CallRecordsPstnUserBlockMode | str] = Field(alias="userBlockMode",default=None,)
	userDisplayName: Optional[str] = Field(alias="userDisplayName",default=None,)
	userId: Optional[str] = Field(alias="userId",default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName",default=None,)
	userTelephoneNumber: Optional[str] = Field(alias="userTelephoneNumber",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .call_records_pstn_user_block_mode import CallRecordsPstnUserBlockMode

