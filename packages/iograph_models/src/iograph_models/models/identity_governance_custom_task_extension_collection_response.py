from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityGovernanceCustomTaskExtensionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[IdentityGovernanceCustomTaskExtension]] = Field(default=None,alias="value",)

from .identity_governance_custom_task_extension import IdentityGovernanceCustomTaskExtension

