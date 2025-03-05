from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ChatMessagePolicyViolation(BaseModel):
	dlpAction: Optional[str | ChatMessagePolicyViolationDlpActionTypes] = Field(alias="dlpAction",default=None,)
	justificationText: Optional[str] = Field(alias="justificationText",default=None,)
	policyTip: Optional[ChatMessagePolicyViolationPolicyTip] = Field(alias="policyTip",default=None,)
	userAction: Optional[str | ChatMessagePolicyViolationUserActionTypes] = Field(alias="userAction",default=None,)
	verdictDetails: Optional[str | ChatMessagePolicyViolationVerdictDetailsTypes] = Field(alias="verdictDetails",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .chat_message_policy_violation_dlp_action_types import ChatMessagePolicyViolationDlpActionTypes
from .chat_message_policy_violation_policy_tip import ChatMessagePolicyViolationPolicyTip
from .chat_message_policy_violation_user_action_types import ChatMessagePolicyViolationUserActionTypes
from .chat_message_policy_violation_verdict_details_types import ChatMessagePolicyViolationVerdictDetailsTypes

