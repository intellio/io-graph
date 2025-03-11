from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityApplyLabelAction(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	actions: SerializeAsAny[Optional[list[SecurityInformationProtectionAction]]] = Field(alias="actions",default=None,)
	actionSource: Optional[SecurityActionSource | str] = Field(alias="actionSource",default=None,)
	responsibleSensitiveTypeIds: Optional[list[str]] = Field(alias="responsibleSensitiveTypeIds",default=None,)
	sensitivityLabelId: Optional[str] = Field(alias="sensitivityLabelId",default=None,)

from .security_information_protection_action import SecurityInformationProtectionAction
from .security_action_source import SecurityActionSource

