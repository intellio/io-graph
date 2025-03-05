from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ChatMessagePolicyViolation(BaseModel):
	dlpAction: Optional[ChatMessagePolicyViolationDlpActionTypes] = Field(default=None,alias="dlpAction",)
	justificationText: Optional[str] = Field(default=None,alias="justificationText",)
	policyTip: Optional[ChatMessagePolicyViolationPolicyTip] = Field(default=None,alias="policyTip",)
	userAction: Optional[ChatMessagePolicyViolationUserActionTypes] = Field(default=None,alias="userAction",)
	verdictDetails: Optional[ChatMessagePolicyViolationVerdictDetailsTypes] = Field(default=None,alias="verdictDetails",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .chat_message_policy_violation_dlp_action_types import ChatMessagePolicyViolationDlpActionTypes
from .chat_message_policy_violation_policy_tip import ChatMessagePolicyViolationPolicyTip
from .chat_message_policy_violation_user_action_types import ChatMessagePolicyViolationUserActionTypes
from .chat_message_policy_violation_verdict_details_types import ChatMessagePolicyViolationVerdictDetailsTypes

