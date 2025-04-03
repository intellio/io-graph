from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class UnsupportedGroupPolicyExtension(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.unsupportedGroupPolicyExtension"] = Field(alias="@odata.type", default="#microsoft.graph.unsupportedGroupPolicyExtension")
	extensionType: Optional[str] = Field(alias="extensionType", default=None,)
	namespaceUrl: Optional[str] = Field(alias="namespaceUrl", default=None,)
	nodeName: Optional[str] = Field(alias="nodeName", default=None,)
	settingScope: Optional[GroupPolicySettingScope | str] = Field(alias="settingScope", default=None,)

from .group_policy_setting_scope import GroupPolicySettingScope
