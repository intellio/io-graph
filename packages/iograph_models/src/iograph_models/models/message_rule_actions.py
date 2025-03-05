from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MessageRuleActions(BaseModel):
	assignCategories: Optional[list[str]] = Field(alias="assignCategories",default=None,)
	copyToFolder: Optional[str] = Field(alias="copyToFolder",default=None,)
	delete: Optional[bool] = Field(alias="delete",default=None,)
	forwardAsAttachmentTo: SerializeAsAny[Optional[list[Recipient]]] = Field(alias="forwardAsAttachmentTo",default=None,)
	forwardTo: SerializeAsAny[Optional[list[Recipient]]] = Field(alias="forwardTo",default=None,)
	markAsRead: Optional[bool] = Field(alias="markAsRead",default=None,)
	markImportance: Optional[str | Importance] = Field(alias="markImportance",default=None,)
	moveToFolder: Optional[str] = Field(alias="moveToFolder",default=None,)
	permanentDelete: Optional[bool] = Field(alias="permanentDelete",default=None,)
	redirectTo: SerializeAsAny[Optional[list[Recipient]]] = Field(alias="redirectTo",default=None,)
	stopProcessingRules: Optional[bool] = Field(alias="stopProcessingRules",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .recipient import Recipient
from .recipient import Recipient
from .importance import Importance
from .recipient import Recipient

