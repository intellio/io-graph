from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MessageRule(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	actions: Optional[MessageRuleActions] = Field(default=None,alias="actions",)
	conditions: Optional[MessageRulePredicates] = Field(default=None,alias="conditions",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	exceptions: Optional[MessageRulePredicates] = Field(default=None,alias="exceptions",)
	hasError: Optional[bool] = Field(default=None,alias="hasError",)
	isEnabled: Optional[bool] = Field(default=None,alias="isEnabled",)
	isReadOnly: Optional[bool] = Field(default=None,alias="isReadOnly",)
	sequence: Optional[int] = Field(default=None,alias="sequence",)

from .message_rule_actions import MessageRuleActions
from .message_rule_predicates import MessageRulePredicates
from .message_rule_predicates import MessageRulePredicates

