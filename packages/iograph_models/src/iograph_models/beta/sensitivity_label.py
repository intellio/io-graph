from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SensitivityLabel(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	applicableTo: Optional[SensitivityLabelTarget | str] = Field(alias="applicableTo",default=None,)
	applicationMode: Optional[ApplicationMode | str] = Field(alias="applicationMode",default=None,)
	assignedPolicies: Optional[list[LabelPolicy]] = Field(alias="assignedPolicies",default=None,)
	autoLabeling: Optional[AutoLabeling] = Field(alias="autoLabeling",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	isDefault: Optional[bool] = Field(alias="isDefault",default=None,)
	isEndpointProtectionEnabled: Optional[bool] = Field(alias="isEndpointProtectionEnabled",default=None,)
	labelActions: SerializeAsAny[Optional[list[LabelActionBase]]] = Field(alias="labelActions",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	priority: Optional[int] = Field(alias="priority",default=None,)
	toolTip: Optional[str] = Field(alias="toolTip",default=None,)
	sublabels: Optional[list[SensitivityLabel]] = Field(alias="sublabels",default=None,)

from .sensitivity_label_target import SensitivityLabelTarget
from .application_mode import ApplicationMode
from .label_policy import LabelPolicy
from .auto_labeling import AutoLabeling
from .label_action_base import LabelActionBase

