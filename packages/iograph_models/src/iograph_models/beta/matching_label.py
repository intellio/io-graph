from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class MatchingLabel(BaseModel):
	applicationMode: Optional[ApplicationMode | str] = Field(alias="applicationMode", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	id: Optional[str] = Field(alias="id", default=None,)
	isEndpointProtectionEnabled: Optional[bool] = Field(alias="isEndpointProtectionEnabled", default=None,)
	labelActions: Optional[list[Annotated[Union[EncryptContent, EncryptWithTemplate, EncryptWithUserDefinedRights, MarkContent, AddFooter, AddHeader, AddWatermark, ProtectGroup, ProtectOnlineMeetingAction, ProtectSite]],Field(discriminator="odata_type")]]] = Field(alias="labelActions", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	policyTip: Optional[str] = Field(alias="policyTip", default=None,)
	priority: Optional[int] = Field(alias="priority", default=None,)
	toolTip: Optional[str] = Field(alias="toolTip", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .application_mode import ApplicationMode
from .encrypt_content import EncryptContent
from .encrypt_with_template import EncryptWithTemplate
from .encrypt_with_user_defined_rights import EncryptWithUserDefinedRights
from .mark_content import MarkContent
from .add_footer import AddFooter
from .add_header import AddHeader
from .add_watermark import AddWatermark
from .protect_group import ProtectGroup
from .protect_online_meeting_action import ProtectOnlineMeetingAction
from .protect_site import ProtectSite

