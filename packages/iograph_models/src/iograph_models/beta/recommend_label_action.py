from __future__ import annotations
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RecommendLabelAction(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	actions: SerializeAsAny[Optional[list[InformationProtectionAction]]] = Field(alias="actions",default=None,)
	actionSource: Optional[ActionSource | str] = Field(alias="actionSource",default=None,)
	label: Optional[LabelDetails] = Field(alias="label",default=None,)
	responsibleSensitiveTypeIds: Optional[list[UUID]] = Field(alias="responsibleSensitiveTypeIds",default=None,)

from .information_protection_action import InformationProtectionAction
from .action_source import ActionSource
from .label_details import LabelDetails

