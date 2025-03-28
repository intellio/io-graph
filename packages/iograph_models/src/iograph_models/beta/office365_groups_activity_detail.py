from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Office365GroupsActivityDetail(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	exchangeMailboxStorageUsedInBytes: Optional[int] = Field(alias="exchangeMailboxStorageUsedInBytes", default=None,)
	exchangeMailboxTotalItemCount: Optional[int] = Field(alias="exchangeMailboxTotalItemCount", default=None,)
	exchangeReceivedEmailCount: Optional[int] = Field(alias="exchangeReceivedEmailCount", default=None,)
	externalMemberCount: Optional[int] = Field(alias="externalMemberCount", default=None,)
	groupDisplayName: Optional[str] = Field(alias="groupDisplayName", default=None,)
	groupId: Optional[str] = Field(alias="groupId", default=None,)
	groupType: Optional[str] = Field(alias="groupType", default=None,)
	isDeleted: Optional[bool] = Field(alias="isDeleted", default=None,)
	lastActivityDate: Optional[str] = Field(alias="lastActivityDate", default=None,)
	memberCount: Optional[int] = Field(alias="memberCount", default=None,)
	ownerPrincipalName: Optional[str] = Field(alias="ownerPrincipalName", default=None,)
	reportPeriod: Optional[str] = Field(alias="reportPeriod", default=None,)
	reportRefreshDate: Optional[str] = Field(alias="reportRefreshDate", default=None,)
	sharePointActiveFileCount: Optional[int] = Field(alias="sharePointActiveFileCount", default=None,)
	sharePointSiteStorageUsedInBytes: Optional[int] = Field(alias="sharePointSiteStorageUsedInBytes", default=None,)
	sharePointTotalFileCount: Optional[int] = Field(alias="sharePointTotalFileCount", default=None,)
	teamsChannelMessagesCount: Optional[int] = Field(alias="teamsChannelMessagesCount", default=None,)
	teamsMeetingsOrganizedCount: Optional[int] = Field(alias="teamsMeetingsOrganizedCount", default=None,)
	yammerLikedMessageCount: Optional[int] = Field(alias="yammerLikedMessageCount", default=None,)
	yammerPostedMessageCount: Optional[int] = Field(alias="yammerPostedMessageCount", default=None,)
	yammerReadMessageCount: Optional[int] = Field(alias="yammerReadMessageCount", default=None,)


