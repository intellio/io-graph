from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class MessageRule(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.messageRule"] = Field(alias="@odata.type", default="#microsoft.graph.messageRule")
	actions: Optional[MessageRuleActions] = Field(alias="actions", default=None,)
	conditions: Optional[MessageRulePredicates] = Field(alias="conditions", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	exceptions: Optional[MessageRulePredicates] = Field(alias="exceptions", default=None,)
	hasError: Optional[bool] = Field(alias="hasError", default=None,)
	isEnabled: Optional[bool] = Field(alias="isEnabled", default=None,)
	isReadOnly: Optional[bool] = Field(alias="isReadOnly", default=None,)
	sequence: Optional[int] = Field(alias="sequence", default=None,)

from .message_rule_actions import MessageRuleActions
from .message_rule_predicates import MessageRulePredicates
