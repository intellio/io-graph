from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MessageRuleActions(BaseModel):
	assignCategories: Optional[list[str]] = Field(default=None,alias="assignCategories",)
	copyToFolder: Optional[str] = Field(default=None,alias="copyToFolder",)
	delete: Optional[bool] = Field(default=None,alias="delete",)
	forwardAsAttachmentTo: Optional[list[Recipient]] = Field(default=None,alias="forwardAsAttachmentTo",)
	forwardTo: Optional[list[Recipient]] = Field(default=None,alias="forwardTo",)
	markAsRead: Optional[bool] = Field(default=None,alias="markAsRead",)
	markImportance: Optional[Importance] = Field(default=None,alias="markImportance",)
	moveToFolder: Optional[str] = Field(default=None,alias="moveToFolder",)
	permanentDelete: Optional[bool] = Field(default=None,alias="permanentDelete",)
	redirectTo: Optional[list[Recipient]] = Field(default=None,alias="redirectTo",)
	stopProcessingRules: Optional[bool] = Field(default=None,alias="stopProcessingRules",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .recipient import Recipient
from .recipient import Recipient
from .importance import Importance
from .recipient import Recipient

