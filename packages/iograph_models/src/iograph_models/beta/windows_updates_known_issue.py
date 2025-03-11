from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdatesKnownIssue(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	knownIssueHistories: Optional[list[WindowsUpdatesKnownIssueHistoryItem]] = Field(alias="knownIssueHistories",default=None,)
	lastUpdatedDateTime: Optional[datetime] = Field(alias="lastUpdatedDateTime",default=None,)
	resolvedDateTime: Optional[datetime] = Field(alias="resolvedDateTime",default=None,)
	safeguardHoldIds: Optional[list[int]] = Field(alias="safeguardHoldIds",default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime",default=None,)
	status: Optional[WindowsUpdatesWindowsReleaseHealthStatus | str] = Field(alias="status",default=None,)
	title: Optional[str] = Field(alias="title",default=None,)
	webViewUrl: Optional[str] = Field(alias="webViewUrl",default=None,)
	originatingKnowledgeBaseArticle: Optional[WindowsUpdatesKnowledgeBaseArticle] = Field(alias="originatingKnowledgeBaseArticle",default=None,)
	resolvingKnowledgeBaseArticle: Optional[WindowsUpdatesKnowledgeBaseArticle] = Field(alias="resolvingKnowledgeBaseArticle",default=None,)

from .windows_updates_known_issue_history_item import WindowsUpdatesKnownIssueHistoryItem
from .windows_updates_windows_release_health_status import WindowsUpdatesWindowsReleaseHealthStatus
from .windows_updates_knowledge_base_article import WindowsUpdatesKnowledgeBaseArticle
from .windows_updates_knowledge_base_article import WindowsUpdatesKnowledgeBaseArticle

