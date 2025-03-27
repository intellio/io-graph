from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UnsupportedGroupPolicyExtension(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	extensionType: Optional[str] = Field(alias="extensionType", default=None,)
	namespaceUrl: Optional[str] = Field(alias="namespaceUrl", default=None,)
	nodeName: Optional[str] = Field(alias="nodeName", default=None,)
	settingScope: Optional[GroupPolicySettingScope | str] = Field(alias="settingScope", default=None,)

from .group_policy_setting_scope import GroupPolicySettingScope

