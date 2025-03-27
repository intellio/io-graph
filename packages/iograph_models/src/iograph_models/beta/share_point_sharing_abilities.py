from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SharePointSharingAbilities(BaseModel):
	anyoneLinkAbilities: Optional[LinkScopeAbilities] = Field(alias="anyoneLinkAbilities", default=None,)
	directSharingAbilities: Optional[DirectSharingAbilities] = Field(alias="directSharingAbilities", default=None,)
	organizationLinkAbilities: Optional[LinkScopeAbilities] = Field(alias="organizationLinkAbilities", default=None,)
	specificPeopleLinkAbilities: Optional[LinkScopeAbilities] = Field(alias="specificPeopleLinkAbilities", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .link_scope_abilities import LinkScopeAbilities
from .direct_sharing_abilities import DirectSharingAbilities
from .link_scope_abilities import LinkScopeAbilities
from .link_scope_abilities import LinkScopeAbilities

