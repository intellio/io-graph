from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class LinkScopeAbilities(BaseModel):
	blockDownloadLinkAbilities: Optional[LinkRoleAbilities] = Field(alias="blockDownloadLinkAbilities", default=None,)
	editLinkAbilities: Optional[LinkRoleAbilities] = Field(alias="editLinkAbilities", default=None,)
	manageListLinkAbilities: Optional[LinkRoleAbilities] = Field(alias="manageListLinkAbilities", default=None,)
	readLinkAbilities: Optional[LinkRoleAbilities] = Field(alias="readLinkAbilities", default=None,)
	reviewLinkAbilities: Optional[LinkRoleAbilities] = Field(alias="reviewLinkAbilities", default=None,)
	submitOnlyLinkAbilities: Optional[LinkRoleAbilities] = Field(alias="submitOnlyLinkAbilities", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .link_role_abilities import LinkRoleAbilities
