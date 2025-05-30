from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class GovernanceNotificationTemplateCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[GovernanceNotificationTemplate]] = Field(alias="value", default=None,)

from .governance_notification_template import GovernanceNotificationTemplate
