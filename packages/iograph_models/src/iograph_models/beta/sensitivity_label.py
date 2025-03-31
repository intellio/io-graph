from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import BaseModel, Field


class SensitivityLabel(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.sensitivityLabel"] = Field(alias="@odata.type",)
	applicableTo: Optional[SensitivityLabelTarget | str] = Field(alias="applicableTo", default=None,)
	applicationMode: Optional[ApplicationMode | str] = Field(alias="applicationMode", default=None,)
	assignedPolicies: Optional[list[LabelPolicy]] = Field(alias="assignedPolicies", default=None,)
	autoLabeling: Optional[AutoLabeling] = Field(alias="autoLabeling", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	isDefault: Optional[bool] = Field(alias="isDefault", default=None,)
	isEndpointProtectionEnabled: Optional[bool] = Field(alias="isEndpointProtectionEnabled", default=None,)
	labelActions: Optional[list[Annotated[Union[EncryptWithTemplate, EncryptWithUserDefinedRights, AddFooter, AddHeader, AddWatermark, ProtectGroup, ProtectOnlineMeetingAction, ProtectSite],Field(discriminator="odata_type")]]] = Field(alias="labelActions", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	priority: Optional[int] = Field(alias="priority", default=None,)
	toolTip: Optional[str] = Field(alias="toolTip", default=None,)
	sublabels: Optional[list[SensitivityLabel]] = Field(alias="sublabels", default=None,)

from .sensitivity_label_target import SensitivityLabelTarget
from .application_mode import ApplicationMode
from .label_policy import LabelPolicy
from .auto_labeling import AutoLabeling
from .encrypt_with_template import EncryptWithTemplate
from .encrypt_with_user_defined_rights import EncryptWithUserDefinedRights
from .add_footer import AddFooter
from .add_header import AddHeader
from .add_watermark import AddWatermark
from .protect_group import ProtectGroup
from .protect_online_meeting_action import ProtectOnlineMeetingAction
from .protect_site import ProtectSite
