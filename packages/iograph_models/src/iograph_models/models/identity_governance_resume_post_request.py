from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Identity_governance_resumePostRequest(BaseModel):
	source: Optional[str] = Field(default=None,alias="source",)
	type: Optional[str] = Field(default=None,alias="type",)
	data: Optional[IdentityGovernanceCustomTaskExtensionCallbackData] = Field(default=None,alias="data",)

from .identity_governance_custom_task_extension_callback_data import IdentityGovernanceCustomTaskExtensionCallbackData

