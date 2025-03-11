from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MatchingLabel(BaseModel):
	applicationMode: Optional[ApplicationMode | str] = Field(alias="applicationMode",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	id: Optional[str] = Field(alias="id",default=None,)
	isEndpointProtectionEnabled: Optional[bool] = Field(alias="isEndpointProtectionEnabled",default=None,)
	labelActions: SerializeAsAny[Optional[list[LabelActionBase]]] = Field(alias="labelActions",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	policyTip: Optional[str] = Field(alias="policyTip",default=None,)
	priority: Optional[int] = Field(alias="priority",default=None,)
	toolTip: Optional[str] = Field(alias="toolTip",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .application_mode import ApplicationMode
from .label_action_base import LabelActionBase

