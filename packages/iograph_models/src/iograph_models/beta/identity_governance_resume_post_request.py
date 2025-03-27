from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Identity_governance_resumePostRequest(BaseModel):
	source: Optional[str] = Field(alias="source", default=None,)
	type: Optional[str] = Field(alias="type", default=None,)
	data: Optional[IdentityGovernanceCustomTaskExtensionCallbackData] = Field(alias="data", default=None,)

from .identity_governance_custom_task_extension_callback_data import IdentityGovernanceCustomTaskExtensionCallbackData

