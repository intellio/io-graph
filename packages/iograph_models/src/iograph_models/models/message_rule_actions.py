from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MessageRuleActions(BaseModel):
	assignCategories: list[Optional[str]] = Field(alias="assignCategories",)
	copyToFolder: Optional[str] = Field(default=None,alias="copyToFolder",)
	delete: Optional[bool] = Field(default=None,alias="delete",)
	forwardAsAttachmentTo: list[Recipient] = Field(alias="forwardAsAttachmentTo",)
	forwardTo: list[Recipient] = Field(alias="forwardTo",)
	markAsRead: Optional[bool] = Field(default=None,alias="markAsRead",)
	markImportance: Optional[Importance] = Field(default=None,alias="markImportance",)
	moveToFolder: Optional[str] = Field(default=None,alias="moveToFolder",)
	permanentDelete: Optional[bool] = Field(default=None,alias="permanentDelete",)
	redirectTo: list[Recipient] = Field(alias="redirectTo",)
	stopProcessingRules: Optional[bool] = Field(default=None,alias="stopProcessingRules",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .recipient import Recipient
from .recipient import Recipient
from .importance import Importance
from .recipient import Recipient

