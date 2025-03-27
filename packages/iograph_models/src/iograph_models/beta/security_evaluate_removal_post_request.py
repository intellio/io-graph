from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Security_evaluate_removalPostRequest(BaseModel):
	contentInfo: Optional[SecurityContentInfo] = Field(alias="contentInfo", default=None,)
	downgradeJustification: Optional[SecurityDowngradeJustification] = Field(alias="downgradeJustification", default=None,)

from .security_content_info import SecurityContentInfo
from .security_downgrade_justification import SecurityDowngradeJustification

